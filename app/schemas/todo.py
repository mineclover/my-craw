from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TodoRead(TodoCreate):
    id: int
    completed: bool
    created_at: datetime

    class Config:
        from_attributes = True  # orm_mode 대신 from_attributes 사용