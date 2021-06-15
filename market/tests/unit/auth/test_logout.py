from market.tests.base_test import BaseTest, db
from flask_login import current_user

class TestLogout(BaseTest):
    def test_logout_route_logs_user_out(self):
        with self.app:
            user = self.app.post('/register', data=dict(username='tester', email_address='test@gmail.com', password1='testing',
                                                 password2='testing'),
                          follow_redirects=True)

            self.assertTrue(current_user.is_active)

            self.app.get('/logout', follow_redirects=True)

            self.assertFalse(current_user.is_active)


    def test_

