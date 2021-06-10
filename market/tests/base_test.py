"""
BaseTest

This class should be the parent class to each non-unit test
It allows for instantiation of the database dynamically
and makes sure that it is a new, blank database each time.
"""
#dsgrdnj
from unittest import TestCase
from market import app
from market import db

class BaseTest(TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
        app.config['WTF_CSRF_ENABLED'] = False
        with app.app_context():
            db.init_app(app)
            db.create_all()
        # Test client
            self.app = app.test_client()
            self.app_context = app.app_context()

    def tearDown(self):
        # Database is blank
        with app.app_context():
            db.session.remove()
            db.drop_all()

