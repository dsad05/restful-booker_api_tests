from api_testing_framework.src.api_client import APIClient
from api_testing_framework.src.request_objects.get_all_bookings_request import GetAllBookingsRequest
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

@pytest.fixture(scope="function")
def auth_token() -> str:
    auth_data = AuthFactory.create_auth_data()
    auth_request = AuthRequest(**auth_data.to_dict())
    response = api_client.post(auth_request)
    assert response.status_code == 200
    return response.json()["token"]

@pytest.fixture(scope="function")
def create_and_delete_booking() -> Generator[int, None, None]:
    booking_data = BookingFactory.create_default_booking()
    create_booking_request = CreateBookingRequest(**booking_data.to_dict())
    response = api_client.post(create_booking_request)
    assert response.status_code == 200
    booking_id = response.json()["bookingid"]
    yield booking_id
    # Teardown: delete booking after test
    auth_data = AuthFactory.create_auth_data()
    auth_request = AuthRequest(**auth_data.to_dict())
    auth_response = api_client.post(auth_request)
    token = auth_response.json()["token"]
    delete_booking_request = DeleteBookingRequest(booking_id=booking_id, token=token)
    api_client.delete(delete_booking_request)


def test_get_all_bookings() -> None:
    request = GetAllBookingsRequest()
    response = api_client.get(request)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_booking(create_and_delete_booking: int) -> None:
    booking_id = create_and_delete_booking
    assert booking_id is not None

def test_get_booking_by_id(create_and_delete_booking: int) -> None:
    booking_id = create_and_delete_booking
    get_booking_request = GetBookingRequest(booking_id=booking_id)
    response = api_client.get(get_booking_request)
    assert response.status_code == 200
    default_booking_data = BookingFactory.create_default_booking()
    assert response.json()["firstname"] == default_booking_data.firstname

def test_update_booking(create_and_delete_booking: int, auth_token: str) -> None:
    booking_id = create_and_delete_booking
    updated_booking_data = BookingFactory.create_updated_booking()
    update_booking_request = UpdateBookingRequest(
        booking_id=booking_id,
        token=auth_token,
        **updated_booking_data.to_dict()
    )
    update_response = api_client.put(update_booking_request)
    assert update_response.status_code == 200
    assert update_response.json()["firstname"] == updated_booking_data.firstname

def test_delete_booking(create_and_delete_booking: int, auth_token: str) -> None:
    booking_id = create_and_delete_booking
    delete_booking_request = DeleteBookingRequest(booking_id=booking_id, token=auth_token)
    delete_response = api_client.delete(delete_booking_request)
    assert delete_response.status_code == 201

    get_booking_request = GetBookingRequest(booking_id=booking_id)
    get_response = api_client.get(get_booking_request)
    assert get_response.status_code == 404