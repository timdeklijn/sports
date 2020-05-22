import pytest
from .test_utils import create_test_client

# Create test client of the API with the test DB
client = create_test_client()

# Add this to the db
TEST_INPUT = {
    "name": "test_name",
    "url": "www.test_example.com",
    "description": "this is a description",
}

# This should be the response from the db
TEST_RESPONSE = {
    "id": 1,
    "name": "test_name",
    "url": "www.test_example.com",
    "description": "this is a description",
}


@pytest.mark.parametrize(
    "test_input, expected",
    [(TEST_INPUT, {"status_code": 200, "response": TEST_RESPONSE})],
)
def test_add_an_exercise(test_input, expected):
    response = client.post("/exercises/", headers={}, json=test_input)
    assert response.status_code == expected["status_code"]
    assert response.json() == expected["response"]


@pytest.mark.parametrize(
    "expected", [{"status_code": 200, "response": [TEST_RESPONSE]}],
)
def test_read_all_exercises(expected):
    response = client.get("/exercises/")
    assert response.status_code == expected["status_code"]
    assert response.json() == expected["response"]


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (1, {"status_code": 200, "response": TEST_RESPONSE}),
        (2, {"status_code": 404, "response": {"message": "Item not Found"}}),
    ],
)
def test_read_an_exercise(test_input, expected):
    response = client.get(f"/exercises/{test_input}")
    assert response.status_code == expected["status_code"]
    assert response.json() == expected["response"]


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (2, {"status_code": 404, "response": {"message": "Item not Found"}}),
        (1, {"status_code": 200, "response": TEST_RESPONSE}),
        (1, {"status_code": 404, "response": {"message": "Item not Found"}}),
    ],
)
def test_remove_an_exercise(test_input, expected):
    response = client.delete(f"/exercises/{test_input}")
    assert response.status_code == expected["status_code"]
    assert response.json() == expected["response"]
