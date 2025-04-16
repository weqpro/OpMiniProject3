from fastapi.testclient import TestClient
from main import app  # заміни на назву свого модуля, якщо інша

client = TestClient(app)


#Aid Requests

def test_search_aid_requests_valid():
    response = client.get("/api/v1/aid_requests/search", params={
        "text": "urgent",
        "tags": ["medical", "supply"]
    })
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_search_aid_requests_missing_text():
    response = client.get("/api/v1/aid_requests/search")
    assert response.status_code == 422


def test_create_aid_request_valid():
    response = client.post("/api/v1/aid_requests/create", json={
        "name": "Need food",
        "description": "Supplies for outpost",
        "tags": ["food", "urgent"],
        "image": "base64string",
        "location": "Sector 7",
        "status": "open",
        "deadline": "2025-04-14T09:49:53.214Z",
        "soldier_id": 1,
        "volunteer_id": 2,
        "category_id": 3
    })
    assert response.status_code == 200


def test_create_aid_request_invalid():
    response = client.post("/api/v1/aid_requests/create", json={})
    assert response.status_code == 422


#Soldiers

def test_create_soldier_valid():
    response = client.post("/api/v1/soldiers/create", json={
        "name": "John",
        "surname": "Doe",
        "email": "john@example.com",
        "password": "securepassword",
        "phone_number": "123456789",
        "unit": "Alpha",
        "subsubunit": "Bravo",
        "battalion": "First"
    })
    assert response.status_code == 200
    assert "email" in response.json()


def test_create_soldier_invalid():
    response = client.post("/api/v1/soldiers/create", json={})
    assert response.status_code == 422


def test_get_all_soldiers():
    response = client.get("/api/v1/soldiers/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


#Auth

def test_login_success():
    response = client.post("/api/auth/token", data={
        "username": "john@example.com",
        "password": "securepassword"
    })
    assert response.status_code == 200


def test_login_invalid():
    response = client.post("/api/auth/token", data={
        "username": "wrong@example.com",
        "password": "wrongpass"
    })
    assert response.status_code in (400, 422)
