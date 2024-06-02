"""Module to define Role schemas."""
from pydantic import BaseModel, ConfigDict

from fastapi_user_management.models.role import RoleNames


class RoleBase(BaseModel):
    """Base Schema for role."""

    name: RoleNames | None = None
    model_config = ConfigDict(from_attributes=True)


class RoleCreate(RoleBase):
    """Schema to create role."""

    name: RoleNames
    model_config = ConfigDict(from_attributes=True)
