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

def test_get_top_people_by_bmi():
    client = TestClient(app)
    response = client.get("/top-people-by-bmi")
    assert response.status_code == 200
    assert 20 == len(response.json())
    assert "name" in response.json()[0]
    assert "bmi" in response.json()[0]
    assert "Dud Bolt" == response.json()[0]['name']
