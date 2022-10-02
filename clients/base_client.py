from utils.config import BASE_URI, BASE_AUTH_URI
from utils.request import APIRequest


class BaseClient:
    def __init__(self):
        self.base_url = BASE_URI
        self.request = APIRequest()
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }


class BaseAuthClient:
    def __init__(self):
        self.base_url = BASE_AUTH_URI
        self.request = APIRequest()
        self.headers = {
            "Content-Type": 'application/json',
            "Accept": 'application/json'
        }

