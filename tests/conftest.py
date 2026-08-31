import os
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="qa",
        choices=["dev", "qa", "prod"],
        help="Environment to run tests against",
    )


@pytest.fixture(scope="session", autouse=True)
def configure_environment(request):
    environment = request.config.getoption("--env")
    os.environ["TEST_ENV"] = environment


@pytest.fixture
def api_client():
    from api.client import APIClient
    return APIClient()


@pytest.fixture
def user_id():
    return 1