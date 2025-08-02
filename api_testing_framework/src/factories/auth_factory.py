from api_testing_framework.src.models.auth_model import AuthData

class AuthFactory:
    @staticmethod
    def create_auth_data() -> AuthData:
        return AuthData(
            username="admin",
            password="password123"
        )

    @staticmethod
    def create_invalid_auth_data() -> AuthData:
        """Returns invalid credentials for negative login tests."""
        return AuthData(
            username="wrong",
            password="wrongpass"
        )

    @staticmethod
    def create_auth_token() -> str:
        """Returns a valid authentication token for use in tests."""
        from api_testing_framework.src.request_objects.auth_request import AuthRequest
        from api_testing_framework.src.api_client import APIClient
        auth_data = AuthFactory.create_auth_data()
        auth_request = AuthRequest(**auth_data.to_dict())
        api_client = APIClient()
        response = api_client.post(auth_request)
        return response.json()["token"]