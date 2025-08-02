from typing import Dict, Any, Optional
from abc import ABC, abstractmethod

class BaseRequest(ABC):
    """
    Abstract base class for all API request objects.
    Defines the interface and common attributes for request objects.
    """
    def __init__(self, path: str, headers: Optional[Dict[str, str]] = None) -> None:
        self.path: str = path
        self.headers: Dict[str, str] = headers if headers is not None else {}

    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """
        Returns the request payload as a dictionary.
        Must be implemented by subclasses.
        """
        pass