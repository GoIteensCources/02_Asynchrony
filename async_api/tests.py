import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_query():
    response = client.get("/query/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from query"}


def test_get_all_users_initial():
    response = client.get("/get_users/")
    assert response.status_code == 200
    assert response.json() == {"users": []}


def test_add_user():
    name = "John"
    response = client.post(f"/get_users/{name}")
    assert response.status_code == 201
    assert response.json() == {"name": name}

    # Проверим, что пользователь добавлен
    response = client.get("/get_users/")
    assert response.status_code == 200
    assert name in response.json()["users"]


def test_add_existing_user():
    name = "John"
    response = client.post(f"/get_users/{name}")
    assert response.status_code == 400
    assert response.json() == {"detail": f"Name '{name}' is exists"}


def test_get_all_users_after_addition():
    response = client.get("/get_users/")
    assert response.status_code == 200
    assert len(response.json()["users"]) > 0
