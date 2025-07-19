from api_testing_framework.src.request_objects.base_request import BaseRequest

class AuthRequest(BaseRequest):
    def __init__(self, username: str, password: str):
        super().__init__(path="/auth", headers={"Content-Type": "application/json"})
        self.username: str = username
        self.password: str = password

    def to_dict(self) -> dict[str, str]:
        return {"username": self.username, "password": self.password}