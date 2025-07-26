from api_testing_framework.src.request_objects.base_request import BaseRequest

class DeleteBookingRequest(BaseRequest):
    def __init__(self, booking_id: int, token: str):
        super().__init__(
            path=f"/booking/{booking_id}",
            headers={"Cookie": f"token={token}"}
        )
        self.booking_id: int = booking_id
        self.token: str = token

    def to_dict(self) -> dict:
        return {"booking_id": self.booking_id, "token": self.token}

    @classmethod
    def invalid(cls) -> "DeleteBookingRequest":
        """Returns a DeleteBookingRequest with invalid data for negative tests."""
        return cls(booking_id=-1, token="invalidtoken")