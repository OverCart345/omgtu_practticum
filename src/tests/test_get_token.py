# test_get_token.py
import pytest
from src.utils.helpers import match_schema
from .base_test import BaseTest

class TestGetToken(BaseTest):

    def test_get_token_success(self):
        response = self.auth_api.get_token()
        assert response.status_code == 200, "Статус код не 200"

        response_json = response.json()
        assert match_schema(response_json, 'src/schemas/auth_schema.json'), "Схема ответа не соответствует ожиданиям"
