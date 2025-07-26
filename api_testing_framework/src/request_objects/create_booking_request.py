from api_testing_framework.src.request_objects.base_request import BaseRequest

class CreateBookingRequest(BaseRequest):
    def __init__(
        self,
        firstname: str,
        lastname: str,
        totalprice: int,
        depositpaid: bool,
        checkin: str,
        checkout: str,
        additionalneeds: str
    ):
        super().__init__(path="/booking")
        self.firstname: str = firstname
        self.lastname: str = lastname
        self.totalprice: int = totalprice
        self.depositpaid: bool = depositpaid
        self.bookingdates: dict[str, str] = {
            "checkin": checkin,
            "checkout": checkout
        }
        self.additionalneeds: str = additionalneeds

    def to_dict(self) -> dict:
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "totalprice": self.totalprice,
            "depositpaid": self.depositpaid,
            "bookingdates": self.bookingdates,
            "additionalneeds": self.additionalneeds
        }

    @classmethod
    def invalid(cls) -> "CreateBookingRequest":
        """Returns a CreateBookingRequest with invalid data for negative tests."""
        return cls(
            firstname="",  # Invalid: empty string
            lastname="",   # Invalid: empty string
            totalprice=-1,  # Invalid: negative price
            depositpaid="notabool",  # Invalid: wrong type
            checkin="invalid-date",  # Invalid: wrong format
            checkout="invalid-date", # Invalid: wrong format
            additionalneeds=None      # Invalid: None instead of str
        )