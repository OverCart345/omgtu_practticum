import pytest
from src.api.auth_api import AuthAPI
from src.api.booking_api import BookingAPI
from src.utils.helpers import match_schema

@pytest.fixture(scope="session")
def auth_api():
    return AuthAPI()

@pytest.fixture(scope="session")
def booking_api():
    return BookingAPI()

@pytest.fixture(scope="session")
def token(auth_api):
    auth_response = auth_api.get_token()
    assert auth_response.status_code == 200, "Не удалось получить токен"
    auth_json = auth_response.json()
    assert match_schema(auth_json, 'src/schemas/auth_schema.json'), "Схема ответа токена не соответствует ожиданиям"
    return auth_json.get('token')

@pytest.fixture
def create_booking(booking_api, token):
    payload = {
        "firstname": "Tema",
        "lastname": "CHepurko",
        "totalprice": 200,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-05-13",
            "checkout": "2024-05-15"
        },
        "additionalneeds": "Lunch"
    }
    response = booking_api.create_booking(payload)
    assert response.status_code == 200, "Не удалось создать бронирование"
    booking = response.json()
    assert match_schema(booking, 'src/schemas/booking_schema.json'), "Схема ответа бронирования не соответствует ожиданиям"
    return booking
