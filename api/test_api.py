from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_read_exercises():
    response = client.get("/exercises/")
    assert response.status_code == 200
