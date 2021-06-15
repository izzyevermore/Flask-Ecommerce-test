from market.tests.base_test import BaseTest, db
from flask import request
from flask_login import current_user


class TestRoutes(BaseTest):
    def test_route_returns_home_page(self):
        with self.app:
            self.app.get('/', follow_redirects=True)

            self.assertIn('/', request.url)

    def test_route_returns_home_page(self):
        with self.app:
            self.app.get('/home', follow_redirects=True)

            self.assertIn('/home', request.url)

    def test_route_returns_market_page(self):
        with self.app:
            self.app.post('/register', data=dict(username='tester', email_address='test@gmail.com', password1='testing',
                                                 password2='testing'),
                          follow_redirects=True)

            self.assertTrue(current_user.is_active)

            self.app.get('/market', follow_redirects=True)

            self.assertIn('/market', request.url)