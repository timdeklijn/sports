from sqlalchemy.orm import Session
import datetime

from . import models, schemas

# Exercises ===========================================================================


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


def remove_exercise(db: Session, exercise_id: int):
    exercise = get_exercise(db, exercise_id)
    if exercise is None:
        return None
    db.delete(exercise)
    db.commit()
    return exercise


# Sessions ============================================================================


def get_sessions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Session).offset(skip).limit(limit).all()


def get_session_by_id(db: Session, session_id: int):
    return db.query(models.Session).filter(models.Session.id == session_id).first()


def create_session(db: Session):
    """
    Add a session with a current time to the database
    """
    db_session = models.Session(
        start_datetime=datetime.datetime.now(), end_datetime=None,
    )
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return db_session.id


def get_open_session_id_or_create(db: Session):
    """
    1. Get all sessions and check for a session without an end date
    2. If there are no sessions (or no sessions without an end date) create a new
        session
    """
    open_session = (
        db.query(models.Session).filter(models.Session.end_datetime == None).all()
    )
    if open_session != []:
        return open_session[-1].id
    return create_session(db)


def remove_session_by_id(db: Session, session_id: int):
    session = get_session_by_id(db, session_id)
    if session is None:
        return None
    db.delete(session)
    db.commit()
    return session


def close_session_by_id(db: Session, session_id):
    session = get_session_by_id(db, session_id)
    session.end_datetime = datetime.datetime.now()
    db.commit()
    return session
