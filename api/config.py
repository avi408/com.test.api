import os
import yaml


def load_config():
    environment = os.getenv("TEST_ENV", "qa")

    config_file = f"config/{environment}.yaml"

    with open(config_file, "r") as file:
        return yaml.safe_load(file)


config = load_config()

BASE_URL = config["api"]["base_url"]
MAX_RESPONSE_TIME = config["api"]["max_response_time"]
AUTH_TOKEN = config["auth"]["token"]
REQUEST_TIMEOUT = config.get("timeout", 10)