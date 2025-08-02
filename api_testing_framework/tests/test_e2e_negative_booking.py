from api_testing_framework.src.api_client import APIClient
from api_testing_framework.src.request_objects.get_booking_request import GetBookingRequest
from api_testing_framework.src.request_objects.auth_request import AuthRequest
from api_testing_framework.src.request_objects.delete_booking_request import DeleteBookingRequest
from api_testing_framework.src.factories.auth_factory import AuthFactory
from api_testing_framework.src.factories.booking_factory import BookingFactory
from typing import Any

api_client = APIClient()

class TestNegativeE2E:
    def test_get_non_existent_booking(self) -> None:
        get_booking_request = GetBookingRequest.invalid()
        response: Any = api_client.get(get_booking_request)
        assert response.status_code == 404

    def test_login_with_invalid_credentials(self) -> None:
        invalid_auth_data = AuthFactory.create_invalid_auth_data()
        auth_request = AuthRequest(**invalid_auth_data.to_dict())
        response: Any = api_client.post(auth_request)
        assert response.status_code == 200
        if response.status_code == 200:
            assert response.json().get("reason") == "Bad credentials"

    def test_delete_non_existent_booking(self) -> None:
        token: str = AuthFactory.create_auth_token()
        delete_request = BookingFactory.delete_non_existent_booking_request(token)
        response: Any = api_client.delete(delete_request)
        assert response.status_code in (404, 405)
