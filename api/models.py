from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    url = Column(String, index=True)
    description = Column(String)

    workouts = relationship("Workout")


class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)
    start_datetime = Column(DateTime)
    end_datetime = Column(DateTime, default=None)

    workouts = relationship("Workout")


class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("sessions.id"))
    exercise_id = Column(Integer, ForeignKey("exercises.id"))
    reps = Column(Integer)
    time = Column(Integer)
    created_at = Column(DateTime)
