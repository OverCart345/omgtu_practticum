import pytest
from src.utils.helpers import match_schema
from .base_test import BaseTest

class TestCreateBooking(BaseTest):

    def test_create_booking_success(self, create_booking):
        self.booking = create_booking
        assert self.booking['booking']['firstname'] == "Tema", "Имя не соответствует ожиданиям"
        # Дополнительные проверки можно добавить здесь
