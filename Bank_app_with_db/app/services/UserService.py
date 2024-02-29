from Bank_app_with_db.app.models.User import User
from Bank_app_with_db.app.models.SilverCard import SilverCard
from Bank_app_with_db.app.models.GoldCard import GoldCard


class UserService:
    user_service = {}
    card_obj = {}

    def __init__(self, name, email, card):
        self.user_service = User(name, email, card)
        self.card_obj = SilverCard(name) if self.user_service.card_id == 1 else GoldCard(name)
        self.card_obj.update_object(self.user_service.limit_amount, self.user_service.loan_amount)

    def display(self):
        self.card_obj.show()

    def withdraw(self, amount):
        print(self.card_obj.withdraw(amount))
        # print(self.user_service.limit_amount)
        print(self.user_service.update(
            {'limit_amount': self.card_obj.limit_amount, 'loan_amount': self.card_obj.loan_amount}))

    def deposit(self, amount):
        print(self.card_obj.deposit(amount))
        print(self.user_service.update(
            {'limit_amount': self.card_obj.limit_amount, 'loan_amount': self.card_obj.loan_amount}))

    def increase_limit(self):
        print(self.card_obj.limit_amount())
        print(self.user_service.update(
            {'limit_amount': self.card_obj.limit_amount, 'loan_amount': self.card_obj.loan_amount}))

    # @staticmethod
    # def find_user_by_email(email):
    #     return User.find_by_email(email)
    #
    # def get_user_by_id(self, user_id):
    #     return self.user_service.find_by_id(user_id)
    #
    # @staticmethod
    # def update_user(user_id, data):
    #     return User.update(user_id, data)
    #
    # @staticmethod
    # def delete_user(user_id):
    #     return User.delete(user_id)
