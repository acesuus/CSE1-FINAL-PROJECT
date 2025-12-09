import json
from app import app

def test_get_all_gms():
    tester = app.test_client()
    response = tester.get("/api/gms/")
    assert response.status_code == 200
