import pytest
from app import app as flask_app


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_index_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Username" in response.data


def test_submit_page(client):
    response = client.post("/submit", data={
        "username": "test_user",
        "password": "test_password"
    })
    assert response.status_code == 200
    assert b"test_user" in response.data
    assert b"test_password" in response.data


def test_query_dinosaurs(client):
    response = client.get("/query?q=dinosaurs")
    assert response.status_code == 200
    assert b"Dinosaurs ruled the Earth 200 million years ago" in response.data


def test_query_unknown(client):
    response = client.get("/query?q=unknown")
    assert response.status_code == 200
    assert b"Unknown" in response.data
