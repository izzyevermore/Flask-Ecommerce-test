from market.tests.base_test import BaseTest, db
from flask import request
from flask_login import current_user


class TestRoutes(BaseTest):
    def test_route_returns_home_page(self):
        with self.app:
            response =  self.app.get('/', follow_redirects=True)

            self.assertIn('/', request.url)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Welcome to Jim Shaped Coding Market', response.data)

    def test_route_returns_home_page(self):
        with self.app:
            response = self.app.get('/home', follow_redirects=True)

            self.assertIn('/home', request.url)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Welcome to Jim Shaped Coding Market', response.data)

    def test_route_returns_market_page(self):
        with self.app:
            self.app.post('/register', data=dict(username='tester', email_address='test@gmail.com', password1='testing',
                                                 password2='testing'),
                          follow_redirects=True)

            self.assertTrue(current_user.is_active)

            response = self.app.get('/market', follow_redirects=True)

            self.assertIn('/market', request.url)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Market Page', response.data)