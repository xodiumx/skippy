from fastapi_users import FastAPIUsers
from fastapi_users.authentication import (
    AuthenticationBackend, CookieTransport, JWTStrategy, )

from main.settings import settings

from .models import User
from .manage import get_user_manager


SECRET = settings.secret_key


def get_jwt_strategy() -> JWTStrategy:
    """Получение JWT - токена."""
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


cookie_transport = CookieTransport(
    cookie_name='auth', cookie_max_age=3600)

auth_backend = AuthenticationBackend(
    name='jwt',
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
