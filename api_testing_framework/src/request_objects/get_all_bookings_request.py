from api_testing_framework.src.request_objects.base_request import BaseRequest

class GetAllBookingsRequest(BaseRequest):
    def __init__(self):
        super().__init__(path="/booking")

    def to_dict(self):
        return {}