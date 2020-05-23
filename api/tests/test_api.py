"""test_api.py

Test all API functionalities
"""

import pytest
from .test_utils import create_test_client

# Create test client of the API with the test DB
client = create_test_client()

# Add this to the db
TEST_EXERCISE_INPUT = {
    "name": "test_name",
    "url": "www.test_example.com",
    "description": "this is a description",
}

# This should be the response from the db
TEST_EXERCISE_RESPONSE = {
    "id": 1,
    "name": "test_name",
    "url": "www.test_example.com",
    "description": "this is a description",
}


@pytest.mark.parametrize(
    "test_input, expected",
    [(TEST_EXERCISE_INPUT, {"status_code": 200, "response": TEST_EXERCISE_RESPONSE})],
)
def test_add_an_exercise(test_input, expected):
    """
    Add an exercise to the database
    """
    response = client.post("/exercises/", headers={}, json=test_input)
    assert response.status_code == expected["status_code"]
    assert response.json() == expected["response"]


@pytest.mark.parametrize(
    "expected", [{"status_code": 200, "response": [TEST_EXERCISE_RESPONSE]}],
)
def test_read_all_exercises(expected):
    """
    Check if the exercise is in the list of all exercises
    """
    response = client.get("/exercises/")
    assert response.status_code == expected["status_code"]
    assert response.json() == expected["response"]


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (1, {"status_code": 200, "response": TEST_EXERCISE_RESPONSE}),
        (2, {"status_code": 404, "response": {"message": "Item not Found"}}),
    ],
)
def test_read_an_exercise(test_input, expected):
    """
    Find the exercise by ID
    """
    response = client.get(f"/exercises/{test_input}")
    assert response.status_code == expected["status_code"]
    assert response.json() == expected["response"]


@pytest.mark.parametrize("expected", [({"status_code": 200, "response": []})])
def test_get_empty_sessions(expected):
    """
    Check if sessions table is empty
    """
    response = client.get("/sessions/")
    assert response.status_code == expected["status_code"]
    assert response.json() == expected["response"]


@pytest.mark.parametrize(
    "expected", [({"status_code": 200, "id": 1}), ({"status_code": 200, "id": 1})]
)
def test_get_id_of_open_session_or_create_new_one(expected):
    """
    Check if a new session is automatically created
    """
    response = client.get("/sessions/current")
    assert response.status_code == expected["status_code"]
    assert response.json()["id"] == expected["id"]


@pytest.mark.parametrize("test_input, expected", [(1, {"status_code": 200, "id": 1})])
def test_get_session_by_id(test_input, expected):
    """
    Check if the session is created
    """
    response = client.get(f"/sessions/{test_input}")
    assert response.status_code == expected["status_code"]
    assert response.json()["id"] == expected["id"]


@pytest.mark.parametrize("expected", [({"status_code": 200, "id": 1})])
def test_get_all_sessions(expected):
    """
    Check if the session is in a list of all session
    """
    response = client.get("/sessions/")
    assert response.status_code == expected["status_code"]
    assert response.json()[0]["id"] == expected["id"]


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ({"reps": 10, "time": None}, {"status_code": 200, "reps": 10, "time": None}),
        ({"reps": None, "time": 10}, {"status_code": 200, "reps": None, "time": 10}),
    ],
)
def test_adding_a_workout_to_a_session(test_input, expected):
    """
    Find a session by id and do a post request to close it
    """
    response = client.post("/sessions/1/exercise/1", headers={}, json=test_input)
    data = response.json()
    assert response.status_code == expected["status_code"]
    assert data["reps"] == expected["reps"]
    assert data["time"] == expected["time"]


def test_closing_a_session_by_id():
    """
    Test closing a session by setting the end_datetime to now
    """
    response = client.get("/sessions/1/close")
    data = response.json()
    assert response.status_code == 200
    assert data["id"] == 1
    assert data["end_datetime"] != None


@pytest.mark.parametrize("expected", [({"status_code": 200, "id": 2})])
def test_get_id_of_open_session_or_create_new_one_after_closing_one(expected):
    """
    Try to find an open session, if not present create a new one.
    """
    response = client.get("/sessions/current")
    assert response.status_code == expected["status_code"]
    assert response.json()["id"] == expected["id"]


def test_get_workout_by_id():
    response = client.get("/workouts/1")
    data = response.json()
    assert response.status_code == 200
    assert data["id"] == 1


def test_get_workout_by_non_existing_id():
    response = client.get("/workouts/100")
    data = response.json()
    assert response.status_code == 404
    assert data == {"message": "Workout not Found"}


def test_get_all_workouts():
    """
    Get a list of all workouts
    """
    response = client.get("/workouts/")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_all_workouts_by_exercise_id():
    response = client.get("/workouts/exercise/1")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_all_workouts_by_non_existing_exercise_id():
    response = client.get("/workouts/exercise/2")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert response.json() == []


@pytest.mark.parametrize(
    "test_input, expected",
    [(1, {"status_code": 200, "id": 1}), (2, {"status_code": 200, "id": 2})],
)
def test_remove_workout_by_id(test_input, expected):
    response = client.delete(f"/workouts/{test_input}")
    assert response.status_code == expected["status_code"]
    assert response.json()["id"] == expected["id"]


def test_remove_workout_by_non_existing_id():
    response = client.delete("/workouts/1")
    assert response.status_code == 404
    assert response.json() == {"message": "Workout not Found"}


@pytest.mark.parametrize(
    "test_input, expected",
    [(3, {"status_code": 404, "response": {"message": "Session not Found"}})],
)
def test_remove_session_by_non_existing_id(test_input, expected):
    """
    Remove a session by ID that does not exist
    """
    response = client.delete(f"/sessions/{test_input}")
    assert response.status_code == expected["status_code"]
    assert response.json() == expected["response"]


@pytest.mark.parametrize(
    "test_input, expected",
    [(1, {"status_code": 200, "id": 1}), (2, {"status_code": 200, "id": 2})],
)
def test_remove_session_by_id(test_input, expected):
    """
    Remove a session by ID that does exist
    """
    response = client.delete(f"/sessions/{test_input}")
    assert response.status_code == expected["status_code"]
    assert response.json()["id"] == expected["id"]


@pytest.mark.parametrize("expected", [({"status_code": 200, "response": []})])
def test_get_empty_sessions_again(expected):
    """
    Test if all sessions are gone
    """
    response = client.get("/sessions/")
    assert response.status_code == expected["status_code"]
    assert response.json() == expected["response"]


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (2, {"status_code": 404, "response": {"message": "Item not Found"}}),
        (1, {"status_code": 200, "response": TEST_EXERCISE_RESPONSE}),
        (1, {"status_code": 404, "response": {"message": "Item not Found"}}),
    ],
)
def test_remove_an_exercise(test_input, expected):
    """
    Remove the exercise from the DB
    """
    response = client.delete(f"/exercises/{test_input}")
    assert response.status_code == expected["status_code"]
    assert response.json() == expected["response"]
