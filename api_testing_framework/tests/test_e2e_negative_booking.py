from api_testing_framework.src.api_client import APIClient
from api_testing_framework.src.request_objects.get_booking_request import GetBookingRequest
import pytest

api_client = APIClient()

class TestNegativeE2E:
    def test_get_non_existent_booking(self):
        non_existent_booking_id = 999999  # Assuming this ID does not exist
        get_booking_request = GetBookingRequest(booking_id=non_existent_booking_id)
        response = api_client.get(get_booking_request.path, headers=get_booking_request.headers)
        assert response.status_code == 404