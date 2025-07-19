from api_testing_framework.src.request_objects.base_request import BaseRequest

class GetBookingRequest(BaseRequest):
    def __init__(self, booking_id):
        super().__init__(path=f"/booking/{booking_id}")
        self.booking_id = booking_id

    def to_dict(self):
        return {} # GET requests typically don't have a body