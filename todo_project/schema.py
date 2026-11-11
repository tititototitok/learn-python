from pydantic import BaseModel, Field
from typing import List, Optional


class SubTodo(BaseModel):
    content: str
    done: bool = False


class Todo(BaseModel):
    id: Optional[int] = None
    content: str = Field(..., min_length=1, max_length=200)
    completed: bool = False
    subtasks: List[SubTodo] = []