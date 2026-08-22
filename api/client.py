import requests

from api.config import BASE_URL, AUTH_TOKEN
from utils.logger import get_logger


logger = get_logger(__name__)


class APIClient:

    def __init__(self):
        self.session = requests.Session()

    def get_user(self, user_id, token=None):
        url = f"{BASE_URL}/users/{user_id}"

        logger.info(f"GET {url}")

        headers = {}

        if token:
            headers["Authorization"] = f"Bearer {token}"

        response = self.session.get(
            url,
            headers=headers
        )

        logger.info(
            f"Response: {response.status_code}"
        )

        return response

    def create_post(self, payload):
        url = f"{BASE_URL}/posts"

        logger.info(f"POST {url}")
        logger.info(f"Payload: {payload}")

        response = self.session.post(
            url,
            json=payload,
            headers={
                "Content-Type": "application/json"
            }
        )

        logger.info(f"Response: {response.status_code}")

        return response

    def update_post(self, post_id, payload):
        url = f"{BASE_URL}/posts/{post_id}"

        logger.info(f"PUT {url}")

        response = self.session.put(
            url,
            json=payload
        )

        logger.info(f"Response: {response.status_code}")

        return response

    def patch_post(self, post_id, payload):
        url = f"{BASE_URL}/posts/{post_id}"

        logger.info(f"PATCH {url}")

        response = self.session.patch(
            url,
            json=payload
        )

        logger.info(f"Response: {response.status_code}")

        return response

    def delete_post(self, post_id):
        url = f"{BASE_URL}/posts/{post_id}"

        logger.info(f"DELETE {url}")

        response = self.session.delete(url)

        logger.info(f"Response: {response.status_code}")

        return response

    def get_posts(self, params=None):
        url = f"{BASE_URL}/posts"

        logger.info(f"GET {url}")
        logger.info(f"Params: {params}")

        response = self.session.get(
            url,
            params=params
        )

        logger.info(f"Response: {response.status_code}")

        return response

    def get_post(self, post_id):
        url = f"{BASE_URL}/posts/{post_id}"

        logger.info(f"GET {url}")

        response = self.session.get(url)

        logger.info(f"Response: {response.status_code}")

        return response