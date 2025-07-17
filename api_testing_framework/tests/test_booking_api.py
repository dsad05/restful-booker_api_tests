from api_testing_framework.src.api_client import APIClient

api_client = APIClient()

def test_get_all_bookings():
    response = api_client.get("/booking")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_booking():
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-05"
        },
        "additionalneeds": "Breakfast"
    }
    response = api_client.post("/booking", json=payload)
    assert response.status_code == 200
    booking_id = response.json()["bookingid"]
    assert booking_id is not None

def test_get_booking_by_id():
    # First, create a booking to get an ID
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-05"
        },
        "additionalneeds": "Breakfast"
    }
    create_response = api_client.post("/booking", json=payload)
    booking_id = create_response.json()["bookingid"]

    response = api_client.get(f"/booking/{booking_id}")
    assert response.status_code == 200
    assert response.json()["firstname"] == "Jim"

def test_update_booking():
    # First, create a booking to get an ID
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-05"
        },
        "additionalneeds": "Breakfast"
    }
    create_response = api_client.post("/booking", json=payload)
    booking_id = create_response.json()["bookingid"]

    # Get auth token
    auth_payload = {
        "username": "admin",
        "password": "password123"
    }
    auth_response = api_client.post("/auth", json=auth_payload)
    token = auth_response.json()["token"]

    update_payload = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 115,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-05"
        },
        "additionalneeds": "Dinner"
    }
    headers = {"Cookie": f"token={token}", "Content-Type": "application/json", "Accept": "application/json"}
    update_response = api_client.put(f"/booking/{booking_id}", json=update_payload, headers=headers)
    assert update_response.status_code == 200
    assert update_response.json()["firstname"] == "James"

def test_delete_booking():
    # First, create a booking to get an ID
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-05"
        },
        "additionalneeds": "Breakfast"
    }
    create_response = api_client.post("/booking", json=payload)
    booking_id = create_response.json()["bookingid"]

    # Get auth token
    auth_payload = {
        "username": "admin",
        "password": "password123"
    }
    auth_response = api_client.post("/auth", json=auth_payload)
    token = auth_response.json()["token"]

    headers = {"Cookie": f"token={token}"}
    delete_response = api_client.delete(f"/booking/{booking_id}", headers=headers)
    assert delete_response.status_code == 201 # 201 No Content for successful delete

    # Verify booking is deleted
    get_response = api_client.get(f"/booking/{booking_id}")
    assert get_response.status_code == 404