from pymongo import MongoClient
from dotenv.main import load_dotenv
import os

# credits from env file
load_dotenv()
user = os.environ['USER_NAME_mongodb']
password = os.environ['PASSWORD_mongodb']


# this is API class to get connection
class ApiServer:
    uri = "mongodb+srv://" + user + ":" + password + "@cluster0.gtmrrte.mongodb.net/?retryWrites=true&w=majority"

    def get_connection(self):
        try:
            client = MongoClient(self.uri)
            print("Connected successfully!!!")
            return client
        except Exception as ex:
            print(f"Could not connect to MongoDB error - {ex}")
