from fastapi import HTTPException, status
from sqladmin import ModelView
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse

from tables import User
from settings import settings


class AdminAuth(AuthenticationBackend):
    """
    Авторизация в админке по:
        - username: в .env
        - password: в .env
    """
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username, password = form['username'], form['password']
        if not (username == settings.admin_username and
                password == settings.admin_password):
                raise HTTPException(
                     status_code=status.HTTP_403_FORBIDDEN,
                     detail='Неверный логин или пароль',
                )
        request.session.update({'token': '...'})
        return True

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> RedirectResponse:
        token = request.session.get('token')
        if not token:
            return RedirectResponse(request.url_for('admin:login'), 
                                    status_code=302)


class UserAdmin(ModelView, model=User):
    """Админ модель пользователя."""
    column_list = (User.id, User.username, User.email)
