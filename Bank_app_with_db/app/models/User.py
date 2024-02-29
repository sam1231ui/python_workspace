from Bank_app_with_db.app.config.db_and_collection import DataBase
from Bank_app_with_db.app.models.SilverCard import SilverCard
from Bank_app_with_db.app.models.GoldCard import GoldCard
import random


class User:
    collection = ""
    _id = 0
    card_id = 0
    username = ""
    email = ""
    limit_amount = 0
    loan_amount = 0

    def __init__(self, username, email, card):
        self.collection = DataBase('BankApp').get_collection('users')
        self.username = username
        self.email = email
        card_obj = SilverCard(username) if card == 1 else GoldCard(username)

        if self.collection.find_one({'email': email, 'card': card}) is None:
            self._id = random.random() * 10000
            self.card = card
            self.limit_amount = card_obj.limit_amount
            self.loan_amount = card_obj.loan_amount
            self.save()
        else:
            data = self.collection.find_one({'email': email, 'card': card})
            self._id = data.get('_id')
            self.card = data.get('card')
            self.loan_amount = data.get('loan_amount')
            self.limit_amount = data.get('limit_amount')

    def save(self):
        return self.collection.insert_one(
            {'_id': self._id, 'username': self.username, 'email': self.email, 'card_id': self.card_id, 'loan_amount': self.loan_amount, 'limit_amount': self.limit_amount})

    def find_by_id(self, user_id):
        return self.collection.find_one({'_id': user_id})

    def find_by_username(self, username):
        return self.collection.find_one({'username': username})

    def update(self, data):
        return self.collection.update_one({'_id': self._id}, {'$set': data})

    def delete(self):
        return self.collection.delete_one({'_id': self._id})
