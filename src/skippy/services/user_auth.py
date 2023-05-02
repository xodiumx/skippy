from datetime import datetime, timedelta

from db import get_session
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.hash import bcrypt
from pydantic import ValidationError
from schemas.user_auth import Token, User, UserCreate
from settings import settings
from sqlalchemy.orm import Session
from tables import User as UserTable

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/sign-in')


def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    """Проверка токена."""
    return AuthService.validate_token(token)


class AuthService:

    @classmethod
    def verify_password(cls, plain_password: str, hash_password: str) -> bool:
        """Проверка сырого пароля с хешированным."""
        return bcrypt.verify(plain_password, hash_password)

    @classmethod
    def hash_password(cls, password: str) -> str:
        """Хеширование пароля."""
        return bcrypt.hash(password)

    @classmethod
    def validate_token(cls, token: str) -> User:
        """валидируем токен"""
        exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Валидация не пройдена',
                headers={
                    'WWW-Authenticate': 'Bearer'
                },
            )
        try:
            payload = jwt.decode(
                token,
                settings.jwt_secret,
                algorithms=(settings.jwt_algorithm),
            )
        except JWTError:
            raise exception from None
        user_data = payload.get('user')
        try:
            user = UserTable.parse_obj(user_data)
        except ValidationError:
            raise exception from None
        return user

    @classmethod
    def create_token(cls, user: User) -> Token:
        """
        Создание jwt токена:
            - iat: время выпуска токена
            - nbf: начало действия токена
            - exp: время истечения токена
            - sub: user_id
            - user: user_data
        """
        user_data = User.from_orm(user)
        now = datetime.utcnow()
        payload = {
            'iat': now,
            'nbf': now,
            'exp': now + timedelta(seconds=settings.jwt_expiration),
            'sub': str(user_data.id),
            'user': user_data.dict(),
        }
        token = jwt.encode(
            payload,
            settings.jwt_secret,
            algorithm=settings.jwt_algorithm,
        )
        return Token(access_token=token)

    def __init__(self, session: Session = Depends(get_session)):
        """Создаем сессию с bd."""
        self.session = session

    def register_new_user(self, user_data: UserCreate) -> Token:
        """
        Регистрация пользователя:
            - Если пользователь с user_data.username или user_data.email exists
              рейзим 400 ошибку
        """
        exception = HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Пользователь с таким username или email существует',
                headers={
                    'WWW-Authenticate': 'Bearer'
                },
            )
        user_exists = (
            self.session
            .query(UserTable)
            .filter(UserTable.username == user_data.username,
                    UserTable.email == user_data.email,)
            .first()
        )
        if user_exists:
            raise exception

        user = UserTable(
            email=user_data.email,
            username=user_data.username,
            password_hash=self.hash_password(user_data.password),
        )
        self.session.add(user)
        self.session.commit()
        return self.create_token(user)

    def authenticate_user(self, username: str, password: str) -> Token:
        """
        Аутентификация пользователя:
            - username
            - password
        """
        exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Неверный username или password',
                headers={
                    'WWW-Authenticate': 'Bearer'
                },
            )
        user = (
            self.session
            .query(UserTable)
            .filter(UserTable.username == username)
            .first()
        )
        if not user:
            raise exception
        if not self.verify_password(password, user.password_hash):
            raise exception
        return self.create_token(user)
