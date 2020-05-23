# Sports App

## The API

### Exercises

- GET `/exercises/` - get all exercises
- GET `/exercises/{exercise_id}` - get a specific exercise
- DELETE `/exercises/{exercise_id}` - remove a specific exercise
- POST `/exercises/` - add an exercise
- [ ] PUT `/exercises/{exercise_id}` - modify a specific exercise

### Sessions

- GET `/sessions/` - get all workout sessions
- GET `/sessions/{session_id}` - get a specific workout session
- DELETE `/sessions/{session_id}` - delete a specific workout session
- [ ] PUT `/sessions/{session_id}` - modify a specific session
- GET `/sessions/current/` - Either add a new exercise of create a new one
- GET `/sessions/{session_id}/close` - Close a specific session
- POST `/sessions/{session_id}/exercise/{exercise_id}` {"reps": int, "times":
  int}

### Workouts

- GET `/workouts/` - get a list of all workouts
- GET `/workouts/{workout_id}` - Get a specific workout
- GET `/workouts/exercise/{exercise_id}` - get a list of all workouts of a
  specific exercise
- [ ] PUT `/workouts/{workout_id}` - modify specific workout
- DELETE `/workouts/{workout_id}` - remove a specific workout

