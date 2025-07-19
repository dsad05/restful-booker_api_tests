from api_testing_framework.src.api_client import APIClient
from api_testing_framework.src.request_objects.base_request import BaseRequest
from api_testing_framework.src.request_objects.get_all_bookings_request import GetAllBookingsRequest
from api_testing_framework.src.request_objects.auth_request import AuthRequest
from api_testing_framework.src.request_objects.create_booking_request import CreateBookingRequest
from api_testing_framework.src.request_objects.get_booking_request import GetBookingRequest
from api_testing_framework.src.request_objects.update_booking_request import UpdateBookingRequest
from api_testing_framework.src.request_objects.delete_booking_request import DeleteBookingRequest
from api_testing_framework.src.factories.booking_factory import BookingFactory
from api_testing_framework.src.factories.auth_factory import AuthFactory
import pytest

api_client = APIClient()

@pytest.fixture(scope="function")
def auth_token():
    auth_data = AuthFactory.create_auth_data()
    auth_request = AuthRequest(**auth_data)
    response = api_client.post(auth_request.path, json=auth_request.to_dict(), headers=auth_request.headers)
    assert response.status_code == 200
    return response.json()["token"]

@pytest.fixture(scope="function")
def create_and_delete_booking():
    booking_data = BookingFactory.create_default_booking()
    create_booking_request = CreateBookingRequest(**booking_data)
    response = api_client.post(create_booking_request.path, json=create_booking_request.to_dict(), headers=create_booking_request.headers)
    assert response.status_code == 200
    booking_id = response.json()["bookingid"]
    yield booking_id
    # Teardown: delete booking after test
    auth_data = AuthFactory.create_auth_data()
    auth_request = AuthRequest(**auth_data)
    auth_response = api_client.post(auth_request.path, json=auth_request.to_dict(), headers=auth_request.headers)
    token = auth_response.json()["token"]
    delete_booking_request = DeleteBookingRequest(booking_id=booking_id, token=token)
    api_client.delete(delete_booking_request.path, headers=delete_booking_request.headers)


def test_get_all_bookings():
    request = GetAllBookingsRequest()
    response = api_client.get(request.path, headers=request.headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_booking(create_and_delete_booking):
    booking_id = create_and_delete_booking
    assert booking_id is not None

def test_get_booking_by_id(create_and_delete_booking):
    booking_id = create_and_delete_booking
    get_booking_request = GetBookingRequest(booking_id=booking_id)
    response = api_client.get(get_booking_request.path, headers=get_booking_request.headers)
    assert response.status_code == 200
    assert response.json()["firstname"] == BookingFactory.create_default_booking()["firstname"]

def test_update_booking(create_and_delete_booking, auth_token):
    booking_id = create_and_delete_booking
    updated_booking_data = BookingFactory.create_updated_booking()
    update_booking_request = UpdateBookingRequest(
        booking_id=booking_id,
        token=auth_token,
        **updated_booking_data
    )
    update_response = api_client.put(update_booking_request.path, json=update_booking_request.to_dict(), headers=update_booking_request.headers)
    assert update_response.status_code == 200
    assert update_response.json()["firstname"] == updated_booking_data["firstname"]

def test_delete_booking(create_and_delete_booking, auth_token):
    booking_id = create_and_delete_booking
    delete_booking_request = DeleteBookingRequest(booking_id=booking_id, token=auth_token)
    delete_response = api_client.delete(delete_booking_request.path, headers=delete_booking_request.headers)
    assert delete_response.status_code == 201

    get_booking_request = GetBookingRequest(booking_id=booking_id)
    get_response = api_client.get(get_booking_request.path, headers=get_booking_request.headers)
    assert get_response.status_code == 404