from My_SQL.config.db_connection import Client
from My_SQL.models.hr_model import HR


# print(client)

class HR_services:

    @staticmethod
    def get_all(table_name):
        return HR.get_all(table_name)

    @staticmethod
    def insert_one_my_table(name, age):
        print("record inserted")
        HR.insert_one(name, age)

    @staticmethod
    def update_age(name, data):
        HR.update_one(name, data)
        return

    @staticmethod
    def pro_call(sp_name):
        HR.pro_call(sp_name)
