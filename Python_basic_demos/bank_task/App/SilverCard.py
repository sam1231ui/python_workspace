import random

from MongoDB.db_connection.db_server_connection import ApiServer

db = ApiServer().get_connection()
print(db)
mydb = db["BankApp"]
my_collection = mydb["users"]


# item = my_collection.find_one({'_id': 0})
# print(item)


class SilverCard:
    limit_amount = 50000
    loan_amount = 0
    name = ""
    _id = 0

    def __init__(self, name):
        self.limit_amount = 50000
        self.loan_amount = 0
        self.name = name
        self._id = int(random.random() * 1000)
        # record = {"_id": self._id, "name": name, "limit_amount": self.limit_amount,
        #           "loan_amount": self.loan_amount, 'card': 2}
        #
        # my_collection.insert_one(record)



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
        return "Service not for silver Card Owner"

    def update_obj(self, limit_amount, loan_amount):
        self.limit_amount = limit_amount
        self.loan_amount = loan_amount

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
