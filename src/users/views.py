from fastapi import Depends, APIRouter

from .utils import fastapi_users
from .models import User

current_user = fastapi_users.current_user()

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)


@router.get('/test-protected')
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.email}"
