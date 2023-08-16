from fastapi.testclient import TestClient

from webapp.src.app import app

def test_get_star_wars_data():
    client = TestClient(app)
    response = client.get("/data/1")
    assert response.status_code == 200
    assert "name" in response.json()

def test_api_http_error():
    client = TestClient(app)
    response = client.get("/data/-1")
    assert response.status_code == 500
