import requests

BASE_URL = "http://127.0.0.1:8000"

def test_health_endpoint():
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_get_existing_user():
    response = requests.get(f"{BASE_URL}/api/v1/users/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Alice"

def test_get_nonexistent_user():
    response = requests.get(f"{BASE_URL}/api/v1/users/999")
    assert response.status_code == 404
    assert "error" in response.json()

def test_create_user_validation_failure():
    payload = {"role": "Tester"}
    response = requests.post(f"{BASE_URL}/api/v1/users", json=payload)
    assert response.status_code == 400
    assert response.json()["error"] == "Missing required field: name"