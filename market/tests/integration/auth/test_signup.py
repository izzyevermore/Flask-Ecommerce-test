from market.models import User
from market.tests.base_test import BaseTest, db
from flask_login import current_user, AnonymousUserMixin

class TestSignUp(BaseTest):
    def test_post_to_register_with_valid_credentials(self):
        with self.app:
            self.app.post('/register', data=dict(username='tester', email_address='test@gmail.com', password1='testing',
                                                 password2='testing'),
                          follow_redirects=True)

            self.assertTrue(current_user.is_active)

