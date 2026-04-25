import json
import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# --- POST /echo ---

def test_post_returns_same_json(client):
    payload = {"name": "John", "age": 30}
    response = client.post(
        "/echo",
        data=json.dumps(payload),
        content_type="application/json",
    )
    assert response.status_code == 200
    assert response.get_json() == payload


def test_post_nested_json(client):
    payload = {"user": {"id": 1, "tags": ["a", "b"]}, "active": True}
    response = client.post(
        "/echo",
        data=json.dumps(payload),
        content_type="application/json",
    )
    assert response.status_code == 200
    assert response.get_json() == payload


def test_post_empty_object(client):
    payload = {}
    response = client.post(
        "/echo",
        data=json.dumps(payload),
        content_type="application/json",
    )
    assert response.status_code == 200
    assert response.get_json() == payload


def test_post_array(client):
    payload = [1, 2, 3]
    response = client.post(
        "/echo",
        data=json.dumps(payload),
        content_type="application/json",
    )
    assert response.status_code == 200
    assert response.get_json() == payload


def test_post_missing_body_returns_400(client):
    response = client.post("/echo", content_type="application/json")
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_post_invalid_json_returns_400(client):
    response = client.post(
        "/echo",
        data="not json",
        content_type="application/json",
    )
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_post_wrong_content_type_returns_400(client):
    response = client.post(
        "/echo",
        data=json.dumps({"key": "value"}),
        content_type="text/plain",
    )
    assert response.status_code == 400
    assert "error" in response.get_json()


# --- GET /echo ---

def test_get_returns_same_json(client):
    payload = {"filter": "active", "page": 1}
    response = client.get(
        "/echo",
        data=json.dumps(payload),
        content_type="application/json",
    )
    assert response.status_code == 200
    assert response.get_json() == payload


def test_get_missing_body_returns_400(client):
    response = client.get("/echo", content_type="application/json")
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_get_invalid_json_returns_400(client):
    response = client.get(
        "/echo",
        data="bad json",
        content_type="application/json",
    )
    assert response.status_code == 400
    assert "error" in response.get_json()


# --- Response headers ---

def test_response_content_type_is_json(client):
    payload = {"ok": True}
    response = client.post(
        "/echo",
        data=json.dumps(payload),
        content_type="application/json",
    )
    assert "application/json" in response.content_type
