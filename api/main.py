"""
==== Exercises ====

GET /exercises/ - get all exercises
GET /exercises/{exercise_id} - get a specific exercise
DELETE /exercises/{exercise_id} - remove a specific exercise
POST /exercises/ - add an exercise
TODO: PUT /exercises/{exercise_id} - modify a specific exercise

==== Sessions ====

GET /sessions/ - get all workout sessions
TODO: GET /sessions/{session_id} - get a specific workout session
TODO: DELETE /sessions/{session_id} - delete a specific workout session
TODO: PUT /sessions/{session_id} - modify a specific session
TODO: GET /sessions/current/ - Either add a new exercise of create a new one
TODO: GET /sessions/close/{session_id} - Close a specific session
TODO: POST /sessions/{session_id}/{exercise_id} {"reps": int, "times": int}

==== Workouts ====

TODO: GET /workouts/ - get a list of all workouts
TODO: GET /workouts/ - Get a specific workout
TODO: GET /workouts/exercise/{exercise_id} - get a list of all workouts of a specific
  exercise
TODO: PUT /workouts/{workout_id} - modify specific workout
TODO: DELETE /workouts/{workout_id} - remove a specific workout
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
