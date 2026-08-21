import requests
import pytest
from api.config import BASE_URL,MAX_RESPONSE_TIME
from jsonschema import validate
from schemas.user_schema import USER_SCHEMA
from api.test_data import (
    POST_PAYLOAD,
    EMPTY_TITLE_PAYLOAD,
    PUT_PAYLOAD,
    PATCH_PAYLOAD
)

def test_get_user(api_client):
    response = api_client.get_user(1)

    assert response.status_code == 200

def test_get_user_response_is_json():
    response = requests.get(
        f"{BASE_URL}/users/1"
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, dict)

def test_user_has_required_fields():
    response = requests.get(
        f"{BASE_URL}/users/1"
    )

    data = response.json()

    assert "id" in data
    assert "name" in data
    assert "username" in data
    assert "email" in data

def test_user_id_is_1():
    response = requests.get(
        f"{BASE_URL}/users/1"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1

    assert data["email"] == "Sincere@april.biz"

def test_create_post(api_client):


    response = api_client.create_post(POST_PAYLOAD)

    data = response.json()

    assert "id" in data
    assert isinstance(data["id"], int)
    assert data["id"] > 0
    assert data["title"] == "QA API Testing"
    assert response.status_code == 201

    data = response.json()

    assert "id" in data
    assert isinstance(data["id"], int)
    assert data["id"] > 0
    assert data["title"] == "QA API Testing"

def test_create_post_with_empty_title(api_client):


    response = api_client.create_post(EMPTY_TITLE_PAYLOAD)

    assert response.status_code == 400

def test_update_post(api_client):

    response = api_client.update_post(1, PUT_PAYLOAD)

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == "Updated QA Test"
    assert data["body"] == "Updated using PUT"
    assert data["userId"] == 1

def test_patch_post(api_client):


    response = api_client.patch_post(1, PATCH_PAYLOAD)

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == "PATCH Updated Title"
    assert data["userId"] == 1

def test_delete_post(api_client):
    response = api_client.delete_post(1)

    assert response.status_code == 200

def test_deleted_post_is_not_available(api_client):
    api_client.delete_post(1)

    response = api_client.get_post(1)

    assert response.status_code == 404



@pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5])
def test_get_multiple_users(api_client, user_id):
    response = api_client.get_user(user_id)

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == user_id
    assert "name" in data
    assert "email" in data

def test_get_user_response_time(api_client):
    response = api_client.get_user(1)

    assert response.status_code == 200
    assert response.elapsed.total_seconds() < MAX_RESPONSE_TIME

def test_user_response_schema(api_client):
    response = api_client.get_user(1)

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data["id"], int)
    assert isinstance(data["name"], str)
    assert isinstance(data["username"], str)
    assert isinstance(data["email"], str)

    assert data["name"] != ""
    assert data["username"] != ""
    assert data["email"] != ""

def test_user_json_schema(api_client):
    response = api_client.get_user(1)

    assert response.status_code == 200

    data = response.json()

    validate(
        instance=data,
        schema=USER_SCHEMA
    )

def test_get_user_content_type(api_client):
    response = api_client.get_user(1)

    assert response.status_code == 200

    content_type = response.headers.get("Content-Type")

    assert content_type is not None
    assert "application/json" in content_type

def test_create_post_with_json_header(api_client):
    response = api_client.create_post(POST_PAYLOAD)

    assert response.status_code == 201
    assert response.request.headers["Content-Type"] == "application/json"

def test_get_user_authorization_header(api_client):
    response = api_client.get_user(
        1,
        token="test-token-123"
    )

    assert response.status_code == 200

    authorization = response.request.headers.get("Authorization")

    assert authorization == "Bearer test-token-123"

def test_get_posts_by_user_id(api_client):
    response = api_client.get_posts(
        {"userId": 1}
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    for post in data:
        assert post["userId"] == 1

def test_get_posts_for_nonexistent_user(api_client):
    response = api_client.get_posts(
        {"userId": 999}
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) == 0