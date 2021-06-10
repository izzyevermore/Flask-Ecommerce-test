from market.tests.base_test import BaseTest, db
from flask_login import current_user, AnonymousUserMixin
from market.models import User
from flask import request

class TestLogin(BaseTest):
    def test_post_to_login_with_valid_credentials(self):
        with self.app:
            self.app.post('/register')
