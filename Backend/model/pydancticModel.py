import datetime

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class todoModel(BaseModel):
    title: str
    description: str
    completed: bool
    time: datetime = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
