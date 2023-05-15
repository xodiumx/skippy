from fastapi import FastAPI
from sqladmin import Admin

#from api.user_auth import router
#from .admin import UserAdmin, AdminAuth, FilmAdmin
from main.settings import settings
from main.db import engine

from users.urls import router as users_router


tags_metadata = [
    {
        'name': 'auth',
        'description': 'Авторизация и регистрация'
    },
    {
        'name': 'films',
        'description': 'films'
    },
]

app = FastAPI(
    title='Skippy',
    description='Description',
    version='0.0.1',
    openapi_tags=tags_metadata,
)


# authentication_backend = AdminAuth(secret_key=settings.secret_key)
# admin = Admin(app, engine, authentication_backend=authentication_backend)

# admin.add_view(UserAdmin)
# admin.add_view(FilmAdmin)
#app.include_router(router)
app.include_router(users_router)