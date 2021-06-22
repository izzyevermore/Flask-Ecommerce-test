from market.tests.base_test import BaseTest, db
from flask_login import current_user, AnonymousUserMixin
from market.models import User
from flask import request

class TestLogin(BaseTest):
    def test_post_to_login_with_valid_credentials(self):
        with self.app:
            self.app.post('/register', data=dict(username='tester', email_address='test@gmail.com', password1='testing', password2='testing'),
                          follow_redirects=True)

            self.assertTrue(current_user.is_active)

            response =  self.app.post('/login', data=dict(username='tester', password='testing'), follow_redirects=True)

            self.assertIn(b'Market Page', response.data)

    def test_post_to_login_with_invalid_credentials(self):
        with self.app:
            self.app.post('/register', data=dict(username='tester', email_address='test@gmail.com', password1='testing',
                                                 password2='testing'),
                          follow_redirects=True)

            self.assertTrue(current_user.is_active)

            response = self.app.post('/login', data=dict(username='tester', password='testin'), follow_redirects=True)

            self.assertIn(b'Username and password are not match!', response.data)

