from abc import ABC, abstractmethod

class BaseRequest(ABC):
    def __init__(self, path: str, headers: dict[str, str] | None = None):
        self.path: str = path
        self.headers: dict[str, str] | None = headers if headers is not None else {}

    @abstractmethod
    def to_dict(self):
        pass