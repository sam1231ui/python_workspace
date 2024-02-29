import random
from MongoDB.db_connection.db_server_connection import ApiServer

db = ApiServer().get_connection()
print(db)
mydb = db["BankApp"]
my_collection = mydb["users"]


class GoldCard:
    limit_amount, loan_amount, maxLimit = 100000, 0, False
    _id = 0

    def __init__(self, name):
        self.limit_amount = self.limit_amount
        self.loan_amount = self.loan_amount
        self.name = name
        self._id = int(random.random() * 1000)
        # record = {"_id": self._id, "name": name, "limit_amount": self.limit_amount,
        #           "loan_amount": self.loan_amount, 'card': 1}
        #
        # my_collection.insert_one(record)

    def update_object(self, limit_amount, loan_amount):
        self.limit_amount = limit_amount
        self.loan_amount = loan_amount

    def show(self):
        print(f"This is limit balance {self.limit_amount}")
        print(f"This is your loan amount {self.loan_amount}")

    def withdraw(self, amount):
        if amount > self.limit_amount:
            return "Not enough amount"
        else:
            self.limit_amount -= amount
            self.loan_amount += amount
            return "transaction Done"

    def deposit(self, amount):
        if self.limit_amount == 0:
            return "No deposit needed"
        else:
            if amount > self.loan_amount:
                return "please deposit required amount not more "
            self.loan_amount -= amount
            self.limit_amount += amount
            return "transaction Done"

    def increase_limit(self):
        if not self.maxLimit:
            self.limit_amount += 50000
            self.maxLimit = True
            return "Limit increased"

        return "Already Increased"

    # all methods with db connection
    # def show_user_details(self):
    #     item = my_collection.find_one({'_id': int(self._id)})
    #     print(item)
    #
    # def withdraw_from_db(self, amount):
    #     if amount > self.limit_amount:
    #         return "Not enough amount"
    #     else:
    #         self.limit_amount -= amount
    #         self.loan_amount += amount
    #         user = {'_id': self._id}
    #         new_amounts = {"$set": {'limit_amount': self.limit_amount,
    #                                 'loan_amount': self.loan_amount}}
    #         my_collection.update_one(user, new_amounts)
    #         return "transaction Done"
    #
    # def deposit_to_db(self, amount):
    #     if self.limit_amount == 0:
    #         return "No deposit needed"
    #     else:
    #         if amount > self.loan_amount:
    #             return "please deposit required amount not more "
    #         self.loan_amount -= amount
    #         self.limit_amount += amount
    #         user = {'_id': self._id}
    #         new_amounts = {"$set": {'limit_amount': self.limit_amount,
    #                                 'loan_amount': self.loan_amount}}
    #         my_collection.update_one(user, new_amounts)
    #         return "transaction Done"
