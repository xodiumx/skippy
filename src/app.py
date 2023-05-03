from fastapi import FastAPI
from sqladmin import Admin

from api.user_auth import router
from admin import UserAdmin, AdminAuth
from settings import settings
from db import engine


tags_metadata = [
    {
        'name': 'auth',
        'description': 'Авторизация и регистрация'
    },
    {
        'name': 'operations',
        'description': 'Работа с операциями'
    },
]

app = FastAPI(
    title='Skippy',
    description='Description',
    version='0.0.1',
    openapi_tags=tags_metadata,
)
authentication_backend = AdminAuth(secret_key=settings.secret_key)
admin = Admin(app, engine, authentication_backend=authentication_backend)

admin.add_view(UserAdmin)
app.include_router(router)
