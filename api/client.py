
import requests
import time

from api.config import BASE_URL, REQUEST_TIMEOUT
from utils.logger import get_logger


logger = get_logger(__name__)


class APIClient:

    def __init__(self):
        self.session = requests.Session()

    def request(
            self,
            method,
            endpoint,
            params=None,
            json=None,
            headers=None,
            token=None,
            timeout=None
    ):
        url = f"{BASE_URL}{endpoint}"

        logger.info(f"{method} {url}")

        if params:
            logger.info(f"Params: {params}")

        if json:
            logger.info(f"Payload: {json}")

        if token:
            headers = headers or {}
            headers["Authorization"] = f"Bearer {token}"

        try:
            start_time = time.perf_counter()

            response = self.session.request(
                method,
                url,
                params=params,
                json=json,
                headers=headers,
                timeout=timeout
            )

            elapsed_time = time.perf_counter() - start_time

            logger.info(f"Response: {response.status_code}")
            logger.info(f"Response time: {elapsed_time:.3f}s")

            return response
        except requests.exceptions.Timeout:
            logger.error(f"Request timed out: {method} {url}")
            raise

        except requests.exceptions.ConnectionError:
            logger.error(f"Connection error: {method} {url}")
            raise

        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {method} {url} - {e}")
            raise
    def get_user(self, user_id, token=None):
        return self.request(
            "GET",
            f"/users/{user_id}",
            token=token,
            timeout=REQUEST_TIMEOUT
        )

    def create_post(self, payload):
        return self.request(
            "POST",
            "/posts",
            json=payload,
            headers={
                "Content-Type": "application/json"
            },
            timeout = REQUEST_TIMEOUT
        )

    def update_post(self, post_id, payload):
        return self.request(
            "PUT",
            f"/posts/{post_id}",
            json=payload,
            timeout=REQUEST_TIMEOUT
        )

    def patch_post(self, post_id, payload):
        return self.request(
            "PATCH",
            f"/posts/{post_id}",
            json=payload,
            timeout=REQUEST_TIMEOUT
        )

    def delete_post(self, post_id):
        return self.request(
            "DELETE",
            f"/posts/{post_id}",
            timeout=REQUEST_TIMEOUT
        )

    def get_posts(self, params=None):
        return self.request(
            "GET",
            "/posts",
            params=params,
            timeout=REQUEST_TIMEOUT
        )

    def get_post(self, post_id):
        return self.request(
            "GET",
            f"/posts/{post_id}",
            timeout=REQUEST_TIMEOUT
        )