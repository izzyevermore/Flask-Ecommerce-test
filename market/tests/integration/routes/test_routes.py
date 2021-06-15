from market.models import Item
from market.models import User
from market.tests.base_test import BaseTest, db
from flask import request
from flask_login import current_user

class TestRoutes(BaseTest):
    def test_post_request_for_user_to_buy_item(self):
        with self.app:
            self.app.post('/register', data=dict(username='tester', email_address='test@gmail.com', password1='testing',
                                            password2='testing'),
                          follow_redirects=True)

            self.assertTrue(current_user.is_active)
            self.assertIn('/market', request.url)
            self.assertTrue(current_user.get_id(), '1')

            user = db.session.query(User).filter_by(username='tester').first()
            self.assertEqual(user.username, 'tester')

            user.budget = 5000
            self.assertEqual(user.budget, 5000)



            item = Item(id=1, name='Phone', price=2000, barcode='testing', description='Model', owner=25)

            db.session.add(item)
            db.session.commit()

            item_exists = db.session.query(Item).filter_by(name='Phone').first()
            self.assertTrue(item_exists)

            response = self.app.post('/market', data=dict(purchased_item='Phone'),follow_redirects=True)

            self.assertIn(b'Congratulations!', response.data)

    def test_post_request_returns_error_message_if_user_has_little_funds(self):
        with self.app:
            self.app.post('/register', data=dict(username='tester', email_address='test@gmail.com', password1='testing',
                                            password2='testing'),
                          follow_redirects=True)

            self.assertTrue(current_user.is_active)
            self.assertIn('/market', request.url)
            self.assertTrue(current_user.get_id(), '1')

            user = db.session.query(User).filter_by(username='tester').first()
            self.assertEqual(user.username, 'tester')


            user.budget = 2000
            self.assertEqual(user.budget, 2000)

            item = Item(id=1, name='Phone', price=3000, barcode='testing', description='Model', owner=25)

            db.session.add(item)
            db.session.commit()


            response = self.app.post('/market', data=dict(purchased_item='Phone'),follow_redirects=True)

            self.assertIn(b'Unfortunately', response.data)


    def test_post_request_to_sell_item_if_user_owns_item(self):
        with self.app:
            self.app.post('/register', data=dict(username='tester', email_address='test@gmail.com', password1='testing',
                                                 password2='testing'),
                          follow_redirects=True)

            self.assertTrue(current_user.is_active)
            self.assertIn('/market', request.url)
            self.assertTrue(current_user.get_id(), '1')

            user = db.session.query(User).filter_by(username='tester').first()
            self.assertEqual(user.username, 'tester')

            item = Item(id=1, name='Phone', price=3000, barcode='testing', description='Model', owner=1)

            db.session.add(item)
            db.session.commit()

            self.assertTrue(user.items, 'Phone')

            response = self.app.post('/market', data=dict(sold_item='Phone'), follow_redirects=True)

            self.assertIn(b'Congratulations!', response.data)


    def test_post_request_to_sell_item_if_user_doesnt_own_item(self):
        with self.app:
            self.app.post('/register', data=dict(username='tester', email_address='test@gmail.com', password1='testing',
                                                 password2='testing'),
                          follow_redirects=True)

            self.assertTrue(current_user.is_active)
            self.assertIn('/market', request.url)
            self.assertTrue(current_user.get_id(), '1')

            user = db.session.query(User).filter_by(username='tester').first()
            self.assertEqual(user.username, 'tester')

            item = Item(id=1, name='Phone', price=3000, barcode='testing', description='Model')

            db.session.add(item)
            db.session.commit()

            self.assertEqual(user.items, [])

            response = self.app.post('/market', data=dict(sold_item='Phone'), follow_redirects=True)

            self.assertIn(b'Something went wrong', response.data)








