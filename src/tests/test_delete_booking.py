# test_delete_booking.py
import pytest
from src.utils.helpers import match_schema
from .base_test import BaseTest

class TestDeleteBooking(BaseTest):

    def test_delete_booking_success(self, create_booking):
        booking_id = create_booking['bookingid']
        response = self.booking_api.delete_booking(booking_id, self.token)
        assert response.status_code == 201, f"Ожидался статус код 201, получен {response.status_code}"

        get_response = self.booking_api.get_booking(booking_id)
        assert get_response.status_code == 404, f"Ожидался статус код 404, получен {get_response.status_code}"
