from api_testing_framework.tests.test_data.auth_data import AuthData

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