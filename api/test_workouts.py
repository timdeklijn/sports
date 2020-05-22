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

# Add an exercise to perform during a workout
client.post("/exercises/", headers={}, json=TEST_EXERCISE_INPUT)


def test_add_a_workout():
    assert 1 == 2


def test_read_all_workouts():
    assert 1 == 2


def test_read_a_single_workout():
    assert 1 == 2


# Remove the exercise added during this test
client.delete("/exercises/1")
