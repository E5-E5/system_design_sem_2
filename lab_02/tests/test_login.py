from fastapi.testclient import TestClient

from src.main import app


client = TestClient(app)


def test_login():

    response = client.post(
        "/auth/login",
        json={
            "login": "admin",
            "password": "123"
        }
    )

    assert response.status_code == 401