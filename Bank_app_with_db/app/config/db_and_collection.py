from Bank_app_with_db.app.config.db_mongo_connection import ApiServer


class DataBase:
    client = ApiServer().get_connection()
    db = ""

    def __init__(self, db):
        self.db = self.client[db]

    def get_collection(self, name):
        collection = self.db[name]
        return collection
