
from datetime import datetime

from pydantic import BaseModel, ConfigDict

class ChangeHistoryResponse(BaseModel):
    id: int
    task_id: int
    user_id: int
    field_name: str
    old_value: str | None
    new_value: str | None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)