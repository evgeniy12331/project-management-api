from datetime import datetime
from pydantic import (BaseModel, Field, EmailStr, ConfigDict)


class UserCreate(BaseModel):
    email: EmailStr
    username: str = Field(min_length=3,max_length=50)
    password: str = Field(min_length=8, max_length=128)

class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)

class UserUpdate(BaseModel):
    email: EmailStr | None = None
    username: str | None = Field(default=None, min_length=3, max_length=50)

class UserAdminUpdate(BaseModel):
    role: str | None = None
    is_active: bool | None = None

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    username: str
    role: str
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

