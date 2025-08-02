from typing import Dict, Any


class BookingData:
    """
    Data object for booking information used in API tests.
    """
    def __init__(
        self,
        firstname: str,
        lastname: str,
        totalprice: int,
        depositpaid: bool,
        checkin: str,
        checkout: str,
        additionalneeds: str
    ) -> None:
        self.firstname: str = firstname
        self.lastname: str = lastname
        self.totalprice: int = totalprice
        self.depositpaid: bool = depositpaid
        self.checkin: str = checkin
        self.checkout: str = checkout
        self.additionalneeds: str = additionalneeds

    def to_dict(self) -> Dict[str, Any]:
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "totalprice": self.totalprice,
            "depositpaid": self.depositpaid,
            "checkin": self.checkin,
            "checkout": self.checkout,
            "additionalneeds": self.additionalneeds
        }
