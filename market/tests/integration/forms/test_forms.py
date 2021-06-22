from wtforms.validators import ValidationError
from market.tests.base_test import BaseTest, db
from market.forms import RegisterForm


class TestForms(BaseTest):
    def test_valid_username(self):
        with self.app:
            # user = User(username='qwerty', email_address='test@gmail.com', password_hash='password')
            self.app.post('/register', data=dict(username='tester', email_address='test@gmail.com',password1='testing', password2='testing')
                          , follow_redirects=True)
            class Username():
                data = 'tester'

            with self.assertRaises(ValidationError) as context:
                RegisterForm().validate_username(Username)
                self.assertEqual('Username already exists! Please try a different username', str(context.exception))

    def test_valid_email(self):
        with self.app:
            self.app.post('/register', data=dict(username='tester', email_address='test@gmail.com',password1='testing', password2='testing'), follow_redirects=True)

            class Email():
                data = 'test@gmail.com'

            with self.assertRaises(ValidationError) as context:
                RegisterForm().validate_email_address(Email)
                self.assertEqual('Email Address already exists! Please try a different email address',
                                 str(context.exception))