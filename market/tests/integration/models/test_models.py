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

