"""User endpoint: /user."""
from typing import Annotated

from fastapi import APIRouter, Depends, status

from fastapi_user_management.models.user import UserModel
from fastapi_user_management.routes import auth
from fastapi_user_management.schemas.user import UserProfile

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"description": "Internal Server Error"},
    },
)


@router.get("/profile", response_model=UserProfile)
async def get_user_profile(
    user: Annotated[UserModel, Depends(auth.get_current_active_user)]
):
    """Get user profile."""
    return user
