"""Tests."""

from fastapi.params import Depends
from fastapi.testclient import TestClient
from sqlalchemy import select
from sqlalchemy.orm import Session

from fastapi_user_management.app import app
from fastapi_user_management.core.database import get_db
from fastapi_user_management.models.role import RoleModel
from fastapi_user_management.models.user import UserModel
from fastapi_user_management.routes.auth import get_current_active_user
from fastapi_user_management.schemas.role import RoleNames
from fastapi_user_management.schemas.user import UserStatusValues


async def get_current_active_user_override(db: Session = Depends(get_db)):
    """Override get_current_active_user dependency."""
    admin_role = db.execute(
        select(RoleModel).where(RoleModel.name == RoleNames.ADMIN)
    ).scalar_one_or_none()
    user = UserModel(
        id=1,
        fullname="admin",
        username="admin@mail.com",
        status=UserStatusValues.ACTIVE,
        roles=[admin_role],
    )

    return user


client = TestClient(app)
app.dependency_overrides[get_current_active_user] = get_current_active_user_override


def test_read_users():
    """Test read users."""
    response = client.get("/admin/user")
    assert response.status_code == 200
