class BookingFactory:
    @staticmethod
    def create_default_booking():
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
    def create_updated_booking():
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
    def create_e2e_default_booking():
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
    def create_e2e_updated_booking():
        return {
            "firstname": "E2E_James",
            "lastname": "E2E_Brown",
            "totalprice": 225,
            "depositpaid": True,
            "checkin": "2024-02-01",
            "checkout": "2024-02-06",
            "additionalneeds": "Late Checkout"
        }