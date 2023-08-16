from fastapi.testclient import TestClient

from webapp.src.app import app

def test_get_top_people_by_bmi():
    client = TestClient(app)
    response = client.get("/top-people-by-bmi")
    assert response.status_code == 200
    assert 20 == len(response.json())
    assert "name" in response.json()[0]
    assert "bmi" in response.json()[0]
    assert "Dud Bolt" == response.json()[0]['name']
