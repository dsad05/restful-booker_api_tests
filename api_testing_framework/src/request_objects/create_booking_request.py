from api_testing_framework.src.request_objects.base_request import BaseRequest

class CreateBookingRequest(BaseRequest):
    def __init__(self, firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds):
        super().__init__(path="/booking")
        self.firstname = firstname
        self.lastname = lastname
        self.totalprice = totalprice
        self.depositpaid = depositpaid
        self.bookingdates = {
            "checkin": checkin,
            "checkout": checkout
        }
        self.additionalneeds = additionalneeds

    def to_dict(self):
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "totalprice": self.totalprice,
            "depositpaid": self.depositpaid,
            "bookingdates": self.bookingdates,
            "additionalneeds": self.additionalneeds
        }