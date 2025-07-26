from api_testing_framework.src.request_objects.base_request import BaseRequest

class UpdateBookingRequest(BaseRequest):
    """
    Request object for updating an existing booking via the API.
    Encapsulates all required fields and headers for the update booking endpoint.
    """
    def __init__(
        self,
        booking_id: int,
        firstname: str,
        lastname: str,
        totalprice: int,
        depositpaid: bool,
        checkin: str,
        checkout: str,
        additionalneeds: str,
        token: str
    ):
        """
        Initialize an UpdateBookingRequest with all required booking fields and authentication token.
        """
        super().__init__(
            path=f"/booking/{booking_id}",
            headers={
                "Cookie": f"token={token}",
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
        )
        self.booking_id: int = booking_id
        self.firstname: str = firstname
        self.lastname: str = lastname
        self.totalprice: int = totalprice
        self.depositpaid: bool = depositpaid
        self.bookingdates: dict[str, str] = {
            "checkin": checkin,
            "checkout": checkout
        }
        self.additionalneeds: str = additionalneeds

    def to_dict(self) -> dict[str, str | int | bool | dict[str, str]]:
        """
        Returns the request payload as a dictionary for the update booking API call.
        """
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "totalprice": self.totalprice,
            "depositpaid": self.depositpaid,
            "bookingdates": self.bookingdates,
            "additionalneeds": self.additionalneeds
        }

    @classmethod
    def invalid(cls) -> "UpdateBookingRequest":
        """
        Returns an UpdateBookingRequest with invalid data for negative test scenarios.
        """
        return cls(
            booking_id=-1,
            firstname="",
            lastname="",
            totalprice=-1,
            depositpaid="notabool",
            checkin="invalid-date",
            checkout="invalid-date",
            additionalneeds=None,
            token="invalidtoken"
        )