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

# Add an exercise to perform during a session
client.post("/exercises/", headers={}, json=TEST_EXERCISE_INPUT)


@pytest.mark.parametrize("expected", [({"status_code": 200, "response": []})])
def test_get_empty_sessions(expected):
    response = client.get("/sessions/")
    assert response.status_code == expected["status_code"]
    assert response.json() == expected["response"]


@pytest.mark.parametrize(
    "expected", [({"status_code": 200, "id": 1}), ({"status_code": 200, "id": 1})]
)
def test_get_id_of_open_session_or_create_new_one(expected):
    response = client.get("/sessions/current")
    assert response.status_code == expected["status_code"]
    assert response.json()["id"] == expected["id"]


@pytest.mark.parametrize("test_input, expected", [(1, {"status_code": 200, "id": 1})])
def test_get_session_by_id(test_input, expected):
    response = client.get(f"/sessions/{test_input}")
    assert response.status_code == expected["status_code"]
    assert response.json()["id"] == expected["id"]


@pytest.mark.parametrize("expected", [({"status_code": 200, "id": 1})])
def test_get_all_sessions(expected):
    response = client.get("/sessions/")
    assert response.status_code == expected["status_code"]
    assert response.json()[0]["id"] == expected["id"]


def test_closing_a_session_by_id():
    """
    Test closing a session by setting the end_datetime to
    now
    """
    response = client.get("/sessions/1/close")
    data = response.json()
    assert response.status_code == 200
    assert data["id"] == 1
    assert data["end_datetime"] != None


@pytest.mark.parametrize("expected", [({"status_code": 200, "id": 2})])
def test_get_id_of_open_session_or_create_new_one_after_closing_one(expected):
    response = client.get("/sessions/current")
    assert response.status_code == expected["status_code"]
    assert response.json()["id"] == expected["id"]


@pytest.mark.parametrize(
    "test_input, expected",
    [(3, {"status_code": 404, "response": {"message": "Session not Found"}})],
)
def test_remove_session_by_non_existing_id(test_input, expected):
    response = client.delete(f"/sessions/{test_input}")
    assert response.status_code == expected["status_code"]
    assert response.json() == expected["response"]


@pytest.mark.parametrize(
    "test_input, expected",
    [(1, {"status_code": 200, "id": 1}), (2, {"status_code": 200, "id": 2})],
)
def test_remove_session_by_id(test_input, expected):
    response = client.delete(f"/sessions/{test_input}")
    assert response.status_code == expected["status_code"]
    assert response.json()["id"] == expected["id"]


@pytest.mark.parametrize("expected", [({"status_code": 200, "response": []})])
def test_get_empty_sessions_again(expected):
    response = client.get("/sessions/")
    assert response.status_code == expected["status_code"]
    assert response.json() == expected["response"]


# Clean up test exercise
client.delete("/exercises/1", headers={}, json=TEST_EXERCISE_INPUT)
