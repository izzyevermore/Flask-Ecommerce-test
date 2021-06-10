from market.tests.base_test import BaseTest, db
from flask_login import current_user, AnonymousUserMixin
from market.models import User
from flask import request

class TestSignUp(BaseTest):
    def test_get_signup_route(self):
        with self.app:
            # Get the route
          response = self.app.get('/register', follow_redirects=True)

        # assert that the url is '/register'
          self.assertIn('/register', request.url)

        #assert that this displays in the '/register' route
          self.assertIn(b'Register Page', response.data)

        # assert that response is 200
          self.assertEqual(response.status_code, 200)

        #assert that no user has signed up
          self.assertEqual(current_user.get_id(), AnonymousUserMixin.get_id(self))

    def test_post_register_with_invalid_email_address(self):
        with self.app:
            response = self.app.post('/register', data=dict(username='tester', email_address='test@gmail.com', password1='testing', password2='testing'),
                          follow_redirects=True)

            self.assertEqual(response.status_code, 200)

            user = db.session.query(User).filter_by(email_address='test@gmail.com')
            self.assertIsNotNone(user)

            response2 = self.app.post('/register', data=dict(username='tester', email_address='test@gmail.com', password1='testing', password2='testing'),
                          follow_redirects=True)

            self.assertIn(b'Email Address already exists!', response2.data)


    def test_post_register_with_same_username(self):
        with self.app:
            response = self.app.post('/register', data=dict(username='tester', email_address='test@gmail.com', password1='testing', password2='testing'),
                          follow_redirects=True)

            # assert that user has been created
            self.assertEqual(response.status_code, 200)

            # #assert that user already exists
            user = db.session.query(User).filter_by(username='tester').first()
            self.assertIsNotNone(user)


             #post again to route
            response2 = self.app.post('/register',data=dict(username='tester', email_address='test@gmail.com', password1='testing', password2='testing'),
                          follow_redirects=True)

            # assert that message appears that user already exists
            self.assertIn(b'Username already exists!', response2.data)

    def test_post_to_register_with_password_less_than_six_characters(self):
        with self.app:
            self.app.post('/register', data=dict(username='tester', email_address='test@gmail.com', password1='test', password2='test'),
                          follow_redirects=True)

            self.assertFalse(current_user.is_active)


