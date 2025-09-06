from fastapi import APIRouter

from app.routes.auth import fastapi_users
from app.schemas.user import UserRead, UserUpdate

router = APIRouter()

# inclui rotas de usuários (GET, PATCH, DELETE)
router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)
