import yaml

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

BASE_URL = config["api"]["base_url"]
MAX_RESPONSE_TIME = config["api"]["max_response_time"]
AUTH_TOKEN = config["auth"]["token"]

REQUEST_TIMEOUT = 10