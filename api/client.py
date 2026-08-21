import requests
from api.config import BASE_URL


class APIClient:

    def __init__(self):
        self.session = requests.Session()

    def get_user(self, user_id):
        return self.session.get(
            f"{BASE_URL}/users/{user_id}"
        )

    def create_post(self, payload):
        return self.session.post(
            f"{BASE_URL}/posts",
            json=payload
        )

    def update_post(self, post_id, payload):
        return self.session.put(
            f"{BASE_URL}/posts/{post_id}",
            json=payload
        )

    def patch_post(self, post_id, payload):
        return self.session.patch(
            f"{BASE_URL}/posts/{post_id}",
            json=payload
        )

    def delete_post(self, post_id):
        return self.session.delete(
            f"{BASE_URL}/posts/{post_id}"
        )

    def get_post(self, post_id):
        return self.session.get(
            f"{BASE_URL}/posts/{post_id}"
        )   