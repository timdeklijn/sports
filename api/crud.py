from sqlalchemy.orm import Session

from . import models, schemas


def get_exercise(db: Session, exercise_id: int):
    return db.query(models.Exercise).filter(models.Exercise.id == exercise_id).first()


def get_exercises(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Exercise).offset(skip).limit(limit).all()


def create_exercise(db: Session, exercise: schemas.ExerciseCreate):
    db_exercise = models.Exercise(
        name=exercise.name, url=exercise.url, description=exercise.description
    )
    db.add(db_exercise)
    db.commit()
    db.refresh(db_exercise)
    return db_exercise
