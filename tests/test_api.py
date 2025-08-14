from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_projects():
    r = client.get("/api/projects/")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert len(data) >= 1

def test_contact_post():
    r = client.post("/api/contact/", json={
        "name": "Test User",
        "email": "test@example.com",
        "subject": "Hello",
        "message": "This is a test"
    })
    assert r.status_code == 200
    assert r.json()["name"] == "Test User"
