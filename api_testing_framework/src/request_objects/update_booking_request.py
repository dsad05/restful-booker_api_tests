from api_testing_framework.src.request_objects.base_request import BaseRequest

class UpdateBookingRequest(BaseRequest):
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
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "totalprice": self.totalprice,
            "depositpaid": self.depositpaid,
            "bookingdates": self.bookingdates,
            "additionalneeds": self.additionalneeds
        }