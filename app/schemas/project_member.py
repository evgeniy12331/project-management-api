from datetime import datetime
from typing import Literal
from pydantic import BaseModel, ConfigDict

class ProjectMemberCreate(BaseModel):
    user_id: int
    role: Literal['manager', 'member'] = 'member'

class ProjectMemberUpdate(BaseModel):
    role: Literal['manager', 'member']

class ProjectMemberResponse(BaseModel):
    id: int
    project_id: int
    user_id: int
    role: str
    joined_at: datetime

    model_config = ConfigDict(from_attributes=True)