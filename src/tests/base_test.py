import pytest
from src.utils.helpers import match_schema

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, auth_api, booking_api, token):
        self.auth_api = auth_api
        self.booking_api = booking_api
        self.token = token
