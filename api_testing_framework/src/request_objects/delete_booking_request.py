from api_testing_framework.src.request_objects.base_request import BaseRequest

class DeleteBookingRequest(BaseRequest):
    def __init__(self, booking_id, token):
        super().__init__(path=f"/booking/{booking_id}", headers={"Cookie": f"token={token}"})
        self.booking_id = booking_id

    def to_dict(self):
        return {} # DELETE requests typically don't have a body