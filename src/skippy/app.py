from api import router
from fastapi import FastAPI

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
    openapi_tags=tags_metadata
)
app.include_router(router)
