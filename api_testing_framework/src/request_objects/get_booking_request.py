from api_testing_framework.src.request_objects.base_request import BaseRequest

class GetBookingRequest(BaseRequest):
    def __init__(self, booking_id: int):
        super().__init__(path=f"/booking/{booking_id}")
        self.booking_id: int = booking_id

    def to_dict(self) -> dict:
        return {"booking_id": self.booking_id}

    @classmethod
    def invalid(cls) -> "GetBookingRequest":
        """Returns a GetBookingRequest with an invalid booking_id for negative tests."""
        return cls(booking_id=-1)