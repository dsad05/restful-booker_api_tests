import requests
from api_testing_framework.src.config import BASE_URL

class APIClient:
    def __init__(self) -> None:
        self.base_url: str = BASE_URL

    def get(self, path: str, params: dict | None = None, headers: dict | None = None) -> requests.Response:
        url = f"{self.base_url}{path}"
        return requests.get(url, params=params, headers=headers)

    def post(self, path: str, json: dict | None = None, headers: dict | None = None) -> requests.Response:
        url = f"{self.base_url}{path}"
        return requests.post(url, json=json, headers=headers)

    def put(self, path: str, json: dict | None = None, headers: dict | None = None) -> requests.Response:
        url = f"{self.base_url}{path}"
        return requests.put(url, json=json, headers=headers)

    def delete(self, path: str, headers: dict | None = None) -> requests.Response:
        url = f"{self.base_url}{path}"
        return requests.delete(url, headers=headers)