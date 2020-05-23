from pydantic import BaseModel
import datetime


class Message(BaseModel):
    message: str


class ID(BaseModel):
    id: int


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


class SessionBase(BaseModel):
    start_datetime: datetime.datetime


class SessionCreate(SessionBase):
    pass


class Session(SessionBase):
    id: int
    end_datetime: datetime.datetime = None

    class Config:
        orm_mode = True


class WorkoutBase(BaseModel):
    time: int = None
    reps: int = None


class WorkoutCreate(WorkoutBase):
    pass


class Workout(WorkoutBase):
    id: int
    session_id: int
    exercise_id: int
    created_at: datetime.datetime

    class Config:
        orm_mode = True
