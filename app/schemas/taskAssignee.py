from datetime import datetime
from pydantic import BaseModel,ConfigDict

class TaskAssigneeCreate(BaseModel):
    user_id: int

class TaskAssigneeResponse(BaseModel):
    id: int
    task_id: int
    user_id: int
    assignee_at: datetime

    model_config = ConfigDict(from_attributes=True)

