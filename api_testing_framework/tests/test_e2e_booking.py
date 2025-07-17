from api_testing_framework.src.api_client import APIClient
import pytest

api_client = APIClient()

@pytest.fixture(scope="module")
def auth_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = api_client.post("/auth", json=payload)
    assert response.status_code == 200
    return response.json()["token"]

@pytest.fixture(scope="module")
def booking_id(auth_token):
    payload = {
        "firstname": "E2E_Jim",
        "lastname": "E2E_Brown",
        "totalprice": 222,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-02-01",
            "checkout": "2024-02-05"
        },
        "additionalneeds": "Parking"
    }
    response = api_client.post("/booking", json=payload)
    assert response.status_code == 200
    booking_id = response.json()["bookingid"]
    yield booking_id
    # Cleanup: delete booking after tests
    headers = {"Cookie": f"token={auth_token}"}
    api_client.delete(f"/booking/{booking_id}", headers=headers)

class TestBookingE2E:
    def test_create_booking(self, booking_id):
        assert booking_id is not None

    def test_get_booking(self, booking_id):
        response = api_client.get(f"/booking/{booking_id}")
        assert response.status_code == 200
        assert response.json()["firstname"] == "E2E_Jim"
        assert response.json()["lastname"] == "E2E_Brown"

    def test_update_booking(self, booking_id, auth_token):
        update_payload = {
            "firstname": "E2E_James",
            "lastname": "E2E_Brown",
            "totalprice": 225,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-02-01",
                "checkout": "2024-02-06"
            },
            "additionalneeds": "Late Checkout"
        }
        headers = {"Cookie": f"token={auth_token}", "Content-Type": "application/json", "Accept": "application/json"}
        response = api_client.put(f"/booking/{booking_id}", json=update_payload, headers=headers)
        assert response.status_code == 200
        assert response.json()["firstname"] == "E2E_James"
        assert response.json()["additionalneeds"] == "Late Checkout"

    def test_delete_booking(self, booking_id, auth_token):
        headers = {"Cookie": f"token={auth_token}"}
        response = api_client.delete(f"/booking/{booking_id}", headers=headers)
        assert response.status_code == 201
        # Verify deletion
        verify_response = api_client.get(f"/booking/{booking_id}")
        assert verify_response.status_code == 404