from .base_request import BaseRequest

class GetAllBookingsRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__(path="/booking")

    def to_dict(self) -> dict:
        return {}

    @classmethod
    def invalid(cls) -> "GetAllBookingsRequest":
        """Returns a GetAllBookingsRequest with an invalid path for negative tests."""
        obj = cls()
        obj.path = "/booking/invalid"  # Purposely invalid path
        return obj