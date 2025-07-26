import requests
from api_testing_framework.src.config import BASE_URL
from api_testing_framework.src.request_objects.base_request import BaseRequest

class APIClient:
    def __init__(self) -> None:
        self.base_url: str = BASE_URL

    def get(self, request: BaseRequest) -> requests.Response:
        url = f"{self.base_url}{request.path}"
        return requests.get(url, headers=request.headers)

    def post(self, request: BaseRequest) -> requests.Response:
        url = f"{self.base_url}{request.path}"
        return requests.post(url, json=request.to_dict(), headers=request.headers)

    def put(self, request: BaseRequest) -> requests.Response:
        url = f"{self.base_url}{request.path}"
        return requests.put(url, json=request.to_dict(), headers=request.headers)

    def delete(self, request: BaseRequest) -> requests.Response:
        url = f"{self.base_url}{request.path}"
        return requests.delete(url, headers=request.headers)