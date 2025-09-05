from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: str = "Не начата"


class TaskCreate(TaskBase):
    """Схема для создания новой задачи."""

    pass


class TaskUpdate(BaseModel):
    """Схема для обновления существующей задачи."""

    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None


class Task(TaskBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
