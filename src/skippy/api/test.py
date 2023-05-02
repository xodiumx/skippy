from fastapi import APIRouter

router = APIRouter(
    prefix='/home',
    tags=['operations']
)

@router.get('/',)
async def home():
    return {'greetings': 'Hello World'}