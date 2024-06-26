"""Module to define User schemas."""
from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr

from fastapi_user_management.models.user import UserStatusValues
from fastapi_user_management.schemas.role import RoleBase


class UserBase(BaseModel):
    """Base Schema for users."""

    fullname: str | None = None
    username: EmailStr | None = None
    status: UserStatusValues | None = None
    roles: list[RoleBase] | None = None
    model_config = ConfigDict(from_attributes=True)


class UserProfile(UserBase):
    """Schema to display user profile."""

    phone_number: str
    model_config = ConfigDict(from_attributes=True)


class UserLogin(BaseModel):
    """Schema use for login request."""

    username: EmailStr
    password: str
    model_config = ConfigDict(from_attributes=True)


class BaseUserCreate(UserBase):
    """Schema to create new user."""

    fullname: str
    username: EmailStr
    password: str | None = None
    roles: list[RoleBase]
    phone_number: str
    last_login: datetime
    model_config = ConfigDict(from_attributes=True)


class UserCreate(BaseUserCreate):
    """Schema to create pre-defined users."""

    fullname: str
    username: EmailStr
    password: str
    phone_number: str
    last_login: datetime
    roles: list[RoleBase]
    model_config = ConfigDict(from_attributes=True)


class UserUpdate(UserBase):
    """Schema to update user password."""

    new_password: str
    new_password_confirm: str
