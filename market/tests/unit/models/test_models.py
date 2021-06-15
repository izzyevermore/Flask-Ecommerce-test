from unittest import TestCase
from market.models import User
from market.models import Item
from market import bcrypt, db


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


    def test_prettier_budget_method(self):
        user = User(username='tester', email_address='test@gmail.com', password_hash='testing', budget=5000).prettier_budget

        self.assertEqual(user, "5,000$")

    def test_password(self):
        user = User(username='tester', email_address='test@gmail.com', password_hash='testing', budget=5000).password_hash

        self.assertEqual(user, 'testing')

    def test_password2(self):
        password = 'testing'
        pw_hash = bcrypt.generate_password_hash(password)

        self.assertTrue(pw_hash, 'testing')

    def test_password_correction(self):
        password = 'testing'
        pw_hash = bcrypt.generate_password_hash(password)

        fake = 'password'
        user = bcrypt.check_password_hash(pw_hash, fake)
        self.assertFalse(user)

    def test_can_purchase_method(self):
        user = User(username='tester', email_address='test@gmail.com', password_hash='testing', budget=5000).can_purchase(Item(
            name='Phone', price=2000, barcode='testing', description='Model'
        ))

        self.assertTrue(user)

    def test_can_sell_method(self):
        item = User(username='tester', email_address='test@gmail.com', password_hash='testing', items=['Phone']).can_sell(
            Item(name='Phone', price=2000, barcode='testing', description='Model')
        )

    def test_item_repr_method(self):
        item = Item(name='Phone', price=2000, barcode='testing', description='Model')

        new_item = item.__repr__()

        self.assertEqual(new_item, 'Item Phone')

    def test_item_buy_method(self):
        user = User(id=1, username='tester', email_address='test@gmail.com', password_hash='testing', budget=5000)

        item = Item(name='Phone', price=2000, barcode='testing', description='Model', owner=1)

        can_buy = item.buy(user)

        db.session.commit()

        self.assertIsNone(can_buy)

    def test_item_sell_method(self):
        user = User(id=1, username='tester', email_address='test@gmail.com', password_hash='testing', budget=5000)

        item = Item(name='Phone', price=2000, barcode='testing', description='Model', owner=1)

        can_sell = item.sell(user)

        db.session.commit()

        self.assertIsNone(can_sell)














