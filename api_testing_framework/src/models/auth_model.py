from typing import Dict


class AuthData:
    """
    Data object for authentication credentials.
    """

    def __init__(self, username: str, password: str) -> None:
        self.username: str = username
        self.password: str = password

    def to_dict(self) -> Dict[str, str]:
        return {
            "username": self.username,
            "password": self.password
        }
