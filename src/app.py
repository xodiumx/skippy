from fastapi import FastAPI

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from sqladmin import Admin
from redis import asyncio as aioredis

#from api.user_auth import router
#from .admin import UserAdmin, AdminAuth, FilmAdmin
from main.settings import settings
from main.db import engine

from users.views import router as users_router
from films.views import router as films_router


tags_metadata = [
    {
        'name': 'auth',
        'description': 'Авторизация и регистрация'
    },
    {
        'name': 'Films',
        'description': 'films'
    },
]

app = FastAPI(
    title='Skippy',
    description='Description',
    version='0.0.1',
    openapi_tags=tags_metadata,
)

@app.on_event("startup")
async def startup():
    """Connect to redis."""
    redis = aioredis.from_url('redis://localhost:14000/0')
    FastAPICache.init(RedisBackend(redis), prefix='fastapi-cache')

# authentication_backend = AdminAuth(secret_key=settings.secret_key)
# admin = Admin(app, engine, authentication_backend=authentication_backend)

# admin.add_view(UserAdmin)
# admin.add_view(FilmAdmin)
#app.include_router(router)
app.include_router(users_router)
app.include_router(films_router)