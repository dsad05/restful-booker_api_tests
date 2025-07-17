import requests
from api_testing_framework.src.config import BASE_URL

class APIClient:
    def __init__(self):
        self.base_url = BASE_URL

    def get(self, path, params=None, headers=None):
        url = f"{self.base_url}{path}"
        return requests.get(url, params=params, headers=headers)

    def post(self, path, json=None, headers=None):
        url = f"{self.base_url}{path}"
        return requests.post(url, json=json, headers=headers)

    def put(self, path, json=None, headers=None):
        url = f"{self.base_url}{path}"
        return requests.put(url, json=json, headers=headers)

    def delete(self, path, headers=None):
        url = f"{self.base_url}{path}"
        return requests.delete(url, headers=headers)