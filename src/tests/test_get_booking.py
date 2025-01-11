# test_get_booking.py
import pytest
from src.utils.helpers import match_schema
from .base_test import BaseTest

class TestGetBooking(BaseTest):

    def test_get_booking_success(self, create_booking):
        booking_id = create_booking['bookingid']
        response = self.booking_api.get_booking(booking_id)
        assert response.status_code == 200, f"Ожидался статус код 200, получен {response.status_code}"

        response_json = response.json()
        assert match_schema(response_json, 'src/schemas/booking_detail_schema.json'), "Схема ответа не соответствует ожиданиям"

        expected = {
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

        for key, value in expected.items():
            assert response_json[key] == value, f"{key} не соответствует ожиданиям"
