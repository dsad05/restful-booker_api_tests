from abc import ABC, abstractmethod

class BaseRequest(ABC):
    """
    Abstract base class for all API request objects.
    Defines the interface and common attributes for request objects.
    """
    def __init__(self, path: str, headers: dict[str, str] | None = None):
        self.path: str = path
        self.headers: dict[str, str] | None = headers if headers is not None else {}

    @abstractmethod
    def to_dict(self) -> dict:
        """
        Returns the request payload as a dictionary.
        Must be implemented by subclasses.
        """
        pass