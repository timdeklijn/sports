from typing import List
from pydantic import BaseModel


class ExerciseBase(BaseModel):
    name: str
    url: str
    description: str


class ExerciseCreate(ExerciseBase):
    pass


class Exercise(ExerciseBase):
    id: int

    class Config:
        orm_mode = True
