import mysql.connector
import os
from dotenv import load_dotenv

# env data loading
load_dotenv()

# all values from env
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


class Client:

    @staticmethod
    def get_connection():
        # Establish MySQL connection
        try:
            connection = mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME
            )

            if connection.is_connected():
                print("Connected to MySQL database")
                return connection

        except mysql.connector.Error as e:
            print("Error while connecting to MySQL", e)
