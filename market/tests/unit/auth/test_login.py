from market.tests.base_test import BaseTest, db
from flask_login import current_user, AnonymousUserMixin
from market.models import User
from flask import request

class TestLogin(BaseTest):
    def test_get_login_page_resp(self):
        with self.app:
            response = self.app.get('/login')

            self.assertIn('/login', request.url)

    def test_get_login_page_returns_with_right_data(self):
        with self.app:
            response = self.app.get('/login')

            self.assertIn(b'Register Page', response.data)