import pytest
from api.client import APIClient


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user_id():
    return 1