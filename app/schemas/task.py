from datetime import datetime
from typing import Literal
from pydantic import BaseModel, Field, ConfigDict

class TaskCreate(BaseModel):
    title: str = Field(min_length=3, max_length=50)
    description: str | None = Field(default=None,max_length=3000)
    priority: Literal['low', 'medium', 'high'] = 'medium'
    due_data: datetime | None = None

class TaskUpdate(BaseModel):
    title: str | None = Field(min_length=3, max_length=50)
    description: str | None = Field(default=None,max_length=500)
    status: Literal['todo', 'in_progress', 'done'] | None = None
    priority: Literal['low', 'medium', 'high'] |  None = None
    due_data: datetime | None = None

class TaskResponse(BaseModel):
    id: int
    project_id: int
    created_by_id: int
    title: str
    description: str
    status: str
    priority: str
    due_data: datetime
    created_at: datetime
    update_at: datetime

    model_config = ConfigDict(from_attributes=True)
