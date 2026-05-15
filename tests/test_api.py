from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_recommend_endpoint():
    response = client.post("/recommend", json={"movie_title": "The Matrix", "top_n": 3})
    assert response.status_code == 200
    assert "recommendations" in response.json()
    assert len(response.json()["recommendations"]) == 3

def test_recommend_not_found():
    response = client.post("/recommend", json={"movie_title": "Non-Existent Movie"})
    assert response.status_code == 404
