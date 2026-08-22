import requests
import pytest
from api.config import BASE_URL,MAX_RESPONSE_TIME
from jsonschema import validate
from schemas.user_schema import USER_SCHEMA
from api.test_data import (
    POST_PAYLOAD,
    EMPTY_TITLE_PAYLOAD,
    PUT_PAYLOAD,
    PATCH_PAYLOAD)

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

    assert response.status_code == 201
    assert response.json()["title"] == ""
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

# def test_deleted_post_is_not_available(api_client):
#     api_client.delete_post(1)
#
#     response = api_client.get_post(1)
#
#     assert response.status_code == 404

# JSONPlaceholder simulates DELETE but does not persist the deletion.
def test_delete_post_does_not_remove_resource_from_jsonplaceholder(api_client):
    delete_response = api_client.delete_post(1)

    assert delete_response.status_code == 200

    get_response = api_client.get_post(1)

    assert get_response.status_code == 200


