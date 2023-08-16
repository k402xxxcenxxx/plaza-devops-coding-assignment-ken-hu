from fastapi.testclient import TestClient

from webapp.src.app import app

def test_get_star_wars_data():
    client = TestClient(app)
    response = client.get("/data/1")
    assert response.status_code == 200
    assert "name" in response.json()

# Additional test cases can be added by the candidate
def test_default_hello():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert "Hello, World!" == response.json()['message']
