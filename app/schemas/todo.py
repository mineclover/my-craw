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
        orm_mode = True 