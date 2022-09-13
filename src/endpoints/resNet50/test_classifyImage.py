from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_auth():
    response = client.get("/auth")
    assert response.status_code == 200
    assert response.json() == {"status": "Authenticated"}

test_auth()