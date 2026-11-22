
from datetime import datetime
from typing import Literal
from pydantic import BaseModel, Field, ConfigDict

class SubtaskCreate(BaseModel):
    title: str = Field(
        min_length=3,
        max_length=200
    )

    description: str | None = Field(
        default=None,
        max_length=5000
    )

class SubtaskUpdate(BaseModel):
    title: str | None = Field(
        default=None,
        min_length=3,
        max_length=200
    )

    description: str | None = Field(
        default=None,
        max_length=5000
    )

    status: Literal["todo", "in_progress", "done"] | None = None

class SubtaskResponse(BaseModel):
    id: int
    task_id: int
    title: str
    description: str | None
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)