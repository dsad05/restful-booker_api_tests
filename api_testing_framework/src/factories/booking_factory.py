class BookingFactory:
    @staticmethod
    def create_default_booking() -> dict:
        return {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "checkin": "2024-01-01",
            "checkout": "2024-01-05",
            "additionalneeds": "Breakfast"
        }

    @staticmethod
    def create_updated_booking() -> dict:
        return {
            "firstname": "James",
            "lastname": "Brown",
            "totalprice": 115,
            "depositpaid": True,
            "checkin": "2024-01-01",
            "checkout": "2024-01-05",
            "additionalneeds": "Dinner"
        }

    @staticmethod
    def create_e2e_default_booking() -> dict:
        return {
            "firstname": "E2E_Jim",
            "lastname": "E2E_Brown",
            "totalprice": 222,
            "depositpaid": True,
            "checkin": "2024-02-01",
            "checkout": "2024-02-05",
            "additionalneeds": "Parking"
        }

    @staticmethod
    def create_e2e_updated_booking() -> dict:
        return {
            "firstname": "E2E_James",
            "lastname": "E2E_Brown",
            "totalprice": 225,
            "depositpaid": True,
            "checkin": "2024-02-01",
            "checkout": "2024-02-06",
            "additionalneeds": "Late Checkout"
        }

    @staticmethod
    def non_existent_booking_id() -> int:
        """Returns a booking ID that should not exist in the system for negative tests."""
        return 999999

    @staticmethod
    def another_non_existent_booking_id() -> int:
        """Returns another booking ID that should not exist in the system for negative tests."""
        return 888888

    @staticmethod
    def delete_non_existent_booking_request(token: str):
        """Returns a DeleteBookingRequest for a non-existent booking ID."""
        from api_testing_framework.src.request_objects.delete_booking_request import DeleteBookingRequest
        return DeleteBookingRequest.non_existent(token=token)