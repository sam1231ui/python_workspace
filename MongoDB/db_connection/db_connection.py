from pymongo import MongoClient

try:
    conn = MongoClient('mongodb://localhost:27017/')
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

db = conn.mydatabase
collection = db.customers1

cursor = collection.find()
print((cursor))
for record in cursor:
    print(type(record))


# myclient = MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["post"]
#
# mydict = { "name": "sam", "address": "Highway 37" }
#
# x = mycol.insert_one(mydict)








