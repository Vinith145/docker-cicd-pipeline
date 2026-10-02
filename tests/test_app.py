"""
Unit tests for the Flask application.
These run in CI on every push.
"""
from app.main import app


def test_home_returns_200():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_home_contains_message():
    client = app.test_client()
    response = client.get("/")
    assert b"Hello from Docker CI/CD pipeline" in response.data


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_version_present():
    client = app.test_client()
    response = client.get("/")
    assert "version" in response.json