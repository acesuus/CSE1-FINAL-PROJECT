import pytest
import json
from app import app
from utils.auth import create_token


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_ECHO'] = False
    client = app.test_client()
    yield client



@pytest.fixture
def auth_headers():
    token = create_token()
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def gm_data():
    """Sample GM data"""
    return {
        "first_name": "rwerwer",
        "last_name": "Ombifdsfsdon",
        "country": "Philippines",
        "birth_year": 2005,
        "peak_rating": 2843,
        "current_rating": 2743,
        "title_year": 2007,
        "FIDE_id": "43243242"
    }


def test_login(client):
    response = client.post("/api/login", json={
        "username": "admin",
        "password": "password123"
    })
    assert response.status_code == 200
    assert "token" in json.loads(response.data)


def test_create_gm(client, auth_headers, gm_data):
    response = client.post("/api/gms/", json=gm_data, headers=auth_headers)
    assert response.status_code == 201


def test_get_all_gms(client):
    response = client.get("/api/gms/")
    assert response.status_code == 200
    assert "grandmasters" in json.loads(response.data)


def test_get_single_gm(client):
    response = client.get("/api/gms/1")
    assert response.status_code in [200, 404]


def test_update_gm(client, auth_headers, gm_data):
    response = client.put("/api/gms/1", json=gm_data, headers=auth_headers)
    assert response.status_code in [200, 404]


def test_delete_gm(client, auth_headers):
    response = client.delete("/api/gms/1", headers=auth_headers)
    assert response.status_code in [200, 404]


def test_no_auth_create(client, gm_data):
    response = client.post("/api/gms/", json=gm_data)
    assert response.status_code == 401


def test_invalid_data(client, auth_headers):
    invalid_gm = {"first_name": 123}
    response = client.post("/api/gms/", json=invalid_gm, headers=auth_headers)
    assert response.status_code == 400


def test_search_gm(client):
    response = client.get("/api/gms/?search=Magnus")
    assert response.status_code == 200
    assert "grandmasters" in json.loads(response.data)


def test_xml_format(client):
    response = client.get("/api/gms/?format=xml")
    assert response.status_code == 200
    assert "application/xml" in response.content_type
