class BookingData:
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
        self.firstname: str = firstname
        self.lastname: str = lastname
        self.totalprice: int = totalprice
        self.depositpaid: bool = depositpaid
        self.checkin: str = checkin
        self.checkout: str = checkout
        self.additionalneeds: str = additionalneeds

    def to_dict(self) -> dict[str, str | int | bool]:
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "totalprice": self.totalprice,
            "depositpaid": self.depositpaid,
            "checkin": self.checkin,
            "checkout": self.checkout,
            "additionalneeds": self.additionalneeds
        }

DEFAULT_BOOKING: BookingData = BookingData(
    firstname="Jim",
    lastname="Brown",
    totalprice=111,
    depositpaid=True,
    checkin="2024-01-01",
    checkout="2024-01-05",
    additionalneeds="Breakfast"
)

UPDATED_BOOKING: BookingData = BookingData(
    firstname="James",
    lastname="Brown",
    totalprice=115,
    depositpaid=True,
    checkin="2024-01-01",
    checkout="2024-01-05",
    additionalneeds="Dinner"
)

E2E_DEFAULT_BOOKING: BookingData = BookingData(
    firstname="E2E_Jim",
    lastname="E2E_Brown",
    totalprice=222,
    depositpaid=True,
    checkin="2024-02-01",
    checkout="2024-02-05",
    additionalneeds="Parking"
)

E2E_UPDATED_BOOKING: BookingData = BookingData(
    firstname="E2E_James",
    lastname="E2E_Brown",
    totalprice=225,
    depositpaid=True,
    checkin="2024-02-01",
    checkout="2024-02-06",
    additionalneeds="Late Checkout"
)
