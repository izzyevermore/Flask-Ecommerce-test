from market.tests.base_test import BaseTest, db
from flask_login import current_user, AnonymousUserMixin
from market.models import User
from flask import request

class TestLogout(BaseTest):
    def test_post_to_logout_redirects_to_home_page(self):
        with self.app:
            resp = self.app.post('/register', data=dict(username='tester', email_address='test@gmail.com', password1='testing',
                                                 password2='testing'),
                          follow_redirects=True)

            self.assertTrue(current_user.is_active)
            self.assertIn(b'Market Page', resp.data)

            response = self.app.get('/logout', follow_redirects=True)

            self.assertIn(b'You have been logged out!', response.data)