from market.tests.base_test import BaseTest, db
from market.models import User, Item


class TestModelsCrud(BaseTest):
    def test_user_crud(self):
            with self.app:
                user = User(username='qwerty', email_address='test@gmail.com', password_hash='password')

                result = db.session.query(User).filter_by(username='qwerty').first()
                self.assertIsNone(result)

                db.session.add(user)
                db.session.commit()

                result = db.session.query(User).filter_by(username='qwerty').first()
                self.assertIsNotNone(result)
                # assert note in db.session

                db.session.delete(user)
                db.session.commit()

                result = db.session.query(User).filter_by(username='qwerty').first()
                self.assertIsNone(result)

    def test_item_crud(self):
        with self.app:
            item = Item(name='paper', price=15, barcode='white', description='test')

            result = db.session.query(Item).filter_by(name='paper').first()
            self.assertIsNone(result)

            db.session.add(item)
            db.session.commit()

            result = db.session.query(Item).filter_by(name='paper').first()
            self.assertIsNotNone(result)
            # assert note in db.session

            db.session.delete(item)
            db.session.commit()

            result = db.session.query(Item).filter_by(name='paper').first()
            self.assertIsNone(result)


    def test_user_can_sell_method(self):
        # register user so that user exists in db
        with self.app:
            response = self.app.post('/register', data=dict(id=1, username='tester', email_address='test@gmail.com', password1='testing',
                                                 password2='testing', items=['Phone']),
                          follow_redirects=True)
        # save item to db
            item = Item(name='Phone', price=2000, barcode='testing', description='Model', owner=1)
            db.session.add(item)
            db.session.commit()

            user = db.session.query(User).filter_by(username='tester').first()

            can_sell = user.can_sell(item)
        # db forms a relationship between an item and user
            self.assertEqual(response.status_code, 200)
            self.assertTrue(can_sell)

    def test_password_setter(self):
        with self.app:
            self.app.post('/register', data=dict(id=1, username='tester', email_address='test@gmail.com', password1='testing',
                                                 password2='testing'), follow_redirects=True)

            user = db.session.query(User).filter_by(username='tester').first()

            password_hash = user.password

            self.assertNotEqual(password_hash, 'testing')

    def test_password_correction_method(self):
        with self.app:
            self.app.post('/register', data=dict(id=1, username='tester', email_address='test@gmail.com', password1='testing',
                                                 password2='testing'), follow_redirects=True)

            user = db.session.query(User).filter_by(username='tester').first()

            password_correction = user.check_password_correction('testing')

            self.assertTrue(password_correction)

            print(password_correction)

    def test_item_buy_method(self):
        with self.app:
            self.app.post('/register', data=dict(id=1, username='tester', email_address='test@gmail.com', password1='testing',
                                                 password2='testing'), follow_redirects=True)

            item = Item(name='Phone', price=2000, barcode='testing', description='Model', owner=5)
            # save this to db
            db.session.add(item)
            db.session.commit()

            user = db.session.query(User).filter_by(username='tester').first()

            user.budget = 5000
            db.session.commit()

            item.buy(user)

            self.assertEqual(user.budget, 3000)
            self.assertEqual(item.owner, 1)


    def test_item_sell_method(self):
        with self.app:
            self.app.post('/register',
                          data=dict(id=1, username='tester', email_address='test@gmail.com', password1='testing',
                                    password2='testing'), follow_redirects=True)

            item = Item(name='Phone', price=2000, barcode='testing', description='Model', owner=5)

            db.session.add(item)
            db.session.commit()

            user = db.session.query(User).filter_by(username='tester').first()

            user.budget = 5000

            db.session.commit()

            item.sell(user)

            self.assertEqual(user.items, [])
            self.assertFalse(item.owner, 1)







