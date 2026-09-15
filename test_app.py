from app import app

def test_home():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 404  # changed from 200 - this will fail