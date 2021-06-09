from unittest import TestCase
from market.models import User
from market.models import Item

class TestModels(TestCase):
    def test_user_model(self):
        user = User(username='tester', email_address='test@gmail.com', password_hash='testing')

        self.assertEqual(user.username, 'tester')
        self.assertEqual(user.password_hash, 'testing')
        self.assertEqual(user.email_address, 'test@gmail.com')


    def test_item_model(self):
        item = Item(name='test', price=20, barcode='testing', description='testing')

        self.assertEqual(item.name, 'test')
        self.assertEqual(item.price, 20)
        self.assertEqual(item.barcode, 'testing')
        self.assertEqual(item.description, 'testing')
