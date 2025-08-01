from api_testing_framework.src.api_client import APIClient
from api_testing_framework.src.request_objects.auth_request import AuthRequest
from api_testing_framework.src.request_objects.create_booking_request import CreateBookingRequest
from api_testing_framework.src.request_objects.get_booking_request import GetBookingRequest
from api_testing_framework.src.request_objects.update_booking_request import UpdateBookingRequest
from api_testing_framework.src.request_objects.delete_booking_request import DeleteBookingRequest
from api_testing_framework.src.factories.booking_factory import BookingFactory
from api_testing_framework.src.factories.auth_factory import AuthFactory
import pytest
from typing import Generator

api_client = APIClient()

@pytest.fixture(scope="module")
def auth_token() -> str:
    auth_data = AuthFactory.create_auth_data()
    auth_request = AuthRequest(**auth_data.to_dict())
    response = api_client.post(auth_request)
    assert response.status_code == 200
    return response.json()["token"]

@pytest.fixture(scope="module")
def booking_id(auth_token: str) -> Generator[int, None, None]:
    booking_data = BookingFactory.create_e2e_default_booking()
    create_booking_request = CreateBookingRequest(**booking_data.to_dict())
    response = api_client.post(create_booking_request)
    assert response.status_code == 200
    booking_id: int = response.json()["bookingid"]
    yield booking_id
    # Cleanup: delete booking after tests
    delete_booking_request = DeleteBookingRequest(booking_id=booking_id, token=auth_token)
    api_client.delete(delete_booking_request)

class TestBookingE2E:
    def test_create_booking(self, booking_id: int) -> None:
        assert booking_id is not None

    def test_get_booking(self, booking_id: int) -> None:
        get_booking_request = GetBookingRequest(booking_id=booking_id)
        response = api_client.get(get_booking_request)
        default_booking_data = BookingFactory.create_e2e_default_booking()
        assert response.status_code == 200
        assert response.json()["firstname"] == default_booking_data.firstname
        assert response.json()["lastname"] == default_booking_data.lastname

    def test_update_booking(self, booking_id: int, auth_token: str) -> None:
        updated_booking_data = BookingFactory.create_e2e_updated_booking()
        update_booking_request = UpdateBookingRequest(
            booking_id=booking_id,
            token=auth_token,
            **updated_booking_data.to_dict()
        )
        response = api_client.put(update_booking_request)
        assert response.status_code == 200
        assert response.json()["firstname"] == updated_booking_data.firstname
        assert response.json()["additionalneeds"] == updated_booking_data.additionalneeds

    def test_delete_booking(self, booking_id: int, auth_token: str) -> None:
        delete_booking_request = DeleteBookingRequest(booking_id=booking_id, token=auth_token)
        response = api_client.delete(delete_booking_request)
        assert response.status_code == 201
        # Verify deletion
        get_booking_request = GetBookingRequest(booking_id=booking_id)
        verify_response = api_client.get(get_booking_request)
        assert verify_response.status_code == 404