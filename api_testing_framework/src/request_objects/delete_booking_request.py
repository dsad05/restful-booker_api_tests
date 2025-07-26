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
    def non_existent(cls, token: str) -> "DeleteBookingRequest":
        """Returns a DeleteBookingRequest for a non-existent booking ID for negative tests."""
        from api_testing_framework.src.factories.booking_factory import BookingFactory
        return cls(booking_id=BookingFactory.non_existent_booking_id(), token=token)