import random

from My_SQL.config.db_connection import Client

# Create cursor
client = Client.get_connection()
my_cursor = client.cursor()


class HR:
    # Execute SQL query
    @staticmethod
    def get_all(table_name):
        query = f"SELECT * FROM {table_name}"
        my_cursor.execute(query)
        rows = my_cursor.fetchall()
        # print(rows)
        return rows

    @staticmethod
    def insert_one(name, age):
        sql = "INSERT INTO my_table (id, name, age) VALUES (%s, %s, %s)"
        val = (int(random.random() * 1000), name, age)
        my_cursor.execute(sql, val)
        client.commit()

    @staticmethod
    def update_one(name, age):
        sql = "UPDATE my_table SET age = (%s) WHERE name = (%s)"
        val = (age, name)
        my_cursor.execute(sql, val)
        client.commit()

    @staticmethod
    def pro_call(sp_name):
        my_cursor.callproc(sp_name, args=())  # Pass any arguments if required
        # Fetch results if any
        for result in my_cursor.stored_results():
            rows = result.fetchall()
            for row in rows:
                print(row)
