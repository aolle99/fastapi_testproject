from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_post_token():
    response = client.post("/users/token", json={
        "grant_type": "password",
        "username": "aolle",
        "password": "1234",
        "scope": ""
    })
    assert response.status_code == 200
    print(response.json())
def test_get_users():
    response = client.get("/users/")
    assert response.status_code == 200


def test_get_users_me():
    response = client.get("/users/me")
    assert response.status_code == 200


def test_create_user():
    response = client.post("/users/", json={
        "username": "test",
        "first_name": "string",
        "last_name": "string",
        "email": "string",
        "password": "1234"
    })
    assert response.status_code == 201


def test_read_user():
    response = client.get("/users/test")
    assert response.status_code == 200


def test_update_user():
    response = client.put("/users/me", json={
        "first_name": "string2",
        "last_name": "string2",
        "email": "string2"
    })
    assert response.status_code == 200
    assert response.json()["first_name"] == "string2"
    assert response.json()["last_name"] == "string2"
    assert response.json()["email"] == "string2"


def test_change_password():
    response = client.put("/users/me/change_password", json={
        "password": "12345"
    })
    assert response.status_code == 200
    assert response.json()["username"] == "test"
    assert response.json()["password"] == "12345"
