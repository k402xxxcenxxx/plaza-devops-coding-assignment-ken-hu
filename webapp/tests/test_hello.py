from fastapi.testclient import TestClient

from webapp.src.app import app

def test_default_hello():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert "Hello, World!" == response.json()['message']
