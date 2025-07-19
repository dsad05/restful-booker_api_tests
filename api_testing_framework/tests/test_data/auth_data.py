class AuthData:
    def __init__(self, username: str, password: str):
        self.username: str = username
        self.password: str = password

    def to_dict(self) -> dict[str, str]:
        return {
            "username": self.username,
            "password": self.password
        }

AUTH_DATA: AuthData = AuthData(
    username="admin",
    password="password123"
)
