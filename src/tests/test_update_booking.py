# test_update_booking.py
import pytest
from src.utils.helpers import match_schema
from .base_test import BaseTest

class TestUpdateBooking(BaseTest):

    def test_update_booking_success(self, create_booking):
        booking_id = create_booking['bookingid']
        update_payload = {
            "firstname": "NeTema",
            "lastname": "NeChepurko",
            "totalprice": 200,  
            "depositpaid": True,  
            "bookingdates": {
                "checkin": "2024-05-13",  
                "checkout": "2024-05-15"  
            },
            "additionalneeds": "Dinner"  
        }
        response = self.booking_api.update_booking(
            booking_id,
            self.token,
            update_payload
        )
        assert response.status_code == 200, f"Ожидался статус код 200, получен {response.status_code}"

        response_json = response.json()
        assert match_schema(response_json, 'src/schemas/booking_detail_schema.json'), "Схема ответа не соответствует ожиданиям"

        expected = {
            "firstname": "NeTema",
            "lastname": "NeChepurko",
            "totalprice": 200,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-05-13",
                "checkout": "2024-05-15"
            },
            "additionalneeds": "Dinner"
        }

        for key, value in expected.items():
            assert response_json[key] == value, f"{key} не соответствует ожиданиям"
