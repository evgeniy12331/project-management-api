from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

class ProjectCreate(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    description: str | None = Field(default=None,max_length=1000)
    status: str | None = Field(default=None,max_length=20)

class ProjectUpdate(BaseModel):
    name: str | None = Field(default=None,min_length=3,max_length=150)
    description: str | None = Field(default=None,max_length=3000)
    status: str | None = Field(default=None, max_length=20)

class ProjectResponse(BaseModel):
    id: int
    name: str
    description: str
    owner_id: int
    status: int
    created_at: datetime
    update_at: datetime

    model_config = ConfigDict(from_attributes=True)


