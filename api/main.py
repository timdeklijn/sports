"""main.py

The full API.
"""

from typing import List

from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Exercises ===========================================================================


@app.get("/exercises/", response_model=List[schemas.Exercise])
def read_exercises(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_exercises(db, skip=skip, limit=limit)


@app.post("/exercises/", response_model=schemas.Exercise)
def create_exercise(exercise: schemas.ExerciseCreate, db: Session = Depends(get_db)):
    return crud.create_exercise(db=db, exercise=exercise)


@app.get(
    "/exercises/{exercise_id}",
    response_model=schemas.Exercise,
    responses={404: {"model": schemas.Message}},
)
def read_exercise(exercise_id: int, db: Session = Depends(get_db)):
    db_exercise = crud.get_exercise(db, exercise_id=exercise_id)
    if db_exercise is None:
        return JSONResponse(status_code=404, content={"message": "Item not Found"})
    return db_exercise


@app.delete(
    "/exercises/{exercise_id}",
    response_model=schemas.Exercise,
    responses={404: {"model": schemas.Message}},
)
def delete_exercise(exercise_id: int, db: Session = Depends(get_db)):
    db_exercise = crud.remove_exercise(db, exercise_id=exercise_id)
    if db_exercise is None:
        return JSONResponse(status_code=404, content={"message": "Item not Found"})
    return db_exercise


# Sessions ============================================================================


@app.get("/sessions/", response_model=List[schemas.Session])
def read_sessions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Read all sessions from the database
    """
    return crud.get_sessions(db, skip=skip, limit=limit)


@app.get("/sessions/current", response_model=schemas.ID)
def check_sessions(db: Session = Depends(get_db)):
    """
    Either return an open session id or create a new one
    """
    return {"id": crud.get_open_session_id_or_create(db)}


@app.get(
    "/sessions/{session_id}/close",
    response_model=schemas.Session,
    responses={404: {"model": schemas.Message}},
)
def close_session(session_id: int, db: Session = Depends(get_db)):
    db_session = crud.close_session_by_id(db, session_id)
    if db_session is None:
        return JSONResponse(status_code=404, content={"message": "Session not Found"})
    return db_session


@app.post(
    "/sessions/{session_id}/exercise/{exercise_id}",
    response_model=schemas.Workout,
    responses={404: {"model": schemas.Message}},
)
def add_workout_to_session(
    session_id: int,
    exercise_id: int,
    workout: schemas.WorkoutCreate,
    db: Session = Depends(get_db),
):
    db_workout = crud.create_workout(
        db, session_id, exercise_id, workout.reps, workout.time
    )
    if db_workout is None:
        return JSONResponse(
            status_code=404, content={"message": "Error inserting workout"}
        )
    return db_workout


@app.get(
    "/sessions/{session_id}",
    response_model=schemas.Session,
    responses={404: {"model": schemas.Message}},
)
def read_session(session_id: int, db: Session = Depends(get_db)):
    db_session = crud.get_session_by_id(db, session_id=session_id)
    if db_session is None:
        return JSONResponse(status_code=404, content={"message": "Session not Found"})
    return db_session


@app.delete(
    "/sessions/{session_id}",
    response_model=schemas.Session,
    responses={404: {"model": schemas.Message}},
)
def delete_session(session_id: int, db: Session = Depends(get_db)):
    db_session = crud.remove_session_by_id(db, session_id=session_id)
    if db_session is None:
        return JSONResponse(status_code=404, content={"message": "Session not Found"})
    return db_session


# Workouts ============================================================================


@app.get("/workouts/", response_model=List[schemas.Workout])
def read_workouts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_workouts(db)


@app.get(
    "/workouts/{workout_id}",
    response_model=schemas.Workout,
    responses={404: {"model": schemas.Message}},
)
def read_workout(workout_id: int, db: Session = Depends(get_db)):
    db_workout = crud.get_workout_by_id(db, workout_id)
    if db_workout is None:
        return JSONResponse(status_code=404, content={"message": "Workout not Found"})
    return db_workout


@app.delete(
    "/workouts/{workout_id}",
    response_model=schemas.Workout,
    responses={404: {"model": schemas.Message}},
)
def delete_workout(workout_id: int, db: Session = Depends(get_db)):
    db_workout = crud.remove_workout_by_id(db, workout_id=workout_id)
    if db_workout is None:
        return JSONResponse(status_code=404, content={"message": "Workout not Found"})
    return db_workout


@app.get(
    "/workouts/exercise/{exercise_id}", response_model=List[schemas.Workout],
)
def get_workouts_by_exercise_id(exercise_id: int, db: Session = Depends(get_db)):
    return crud.get_workout_by_exercise(db, exercise_id=exercise_id)
