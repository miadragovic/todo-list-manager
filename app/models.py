from pydantic import BaseModel
from typing import Optional
from enum import Enum

class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    priority: Priority
