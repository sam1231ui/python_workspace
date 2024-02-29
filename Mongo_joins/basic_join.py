from Bank_app_with_db.app.config.db_and_collection import DataBase

# database connection
client = DataBase("myDatabase")

# define pipeline
pipeline1 = [
    {
        '$lookup': {
            'from': 'inventory',
            'localField': 'prodId',
            'foreignField': 'prodId',
            'as': 'inventoryDocs'
        }
    },
    {
        '$project': {
            '_id': 0,
            'prodId': 1,
            'orderId': 1,
            'numPurchased': 1,
            'price': '$inventoryDocs.price'
        }
    },
    {
        '$unwind': {
            'path': '$price'
        }
    }
]

pipeline2 = [
    {
        '$lookup': {
            'from': 'orders',
            'localField': 'prodId',
            'foreignField': 'prodId',
            'as': 'orders'
        }
    },
    {
        '$unwind': '$orders'
    },
    {
        '$project': {
            '_id': 0,
            'prodId': 1,
            'orderId': '$orders.orderId',
            'numPurchased': '$orders.numPurchased',
            'price': 1
        }
    }
]

# pipline3 = [
#     {
#         '$group':
#             {
#                 '_id': "$prodId",
#                 'amountSold': {'$sum': {'$multiply': ['$price', '$numPurchased']}}
#             }
#     }
# ]

# Execute the aggregation pipeline
result = client.get_collection("orders").aggregate(pipeline1)
result2 = client.get_collection("orders").aggregate(pipeline2)
# result3 = client.get_collection("orders").aggregate(pipline3)

# Print the results
for doc in result:
    print(doc)

print("\nThis is 2nd pipeline result")
for data in result2:
    print(data)

# print("\nThis is 3rd pipeline result")
# for x in result3:
#     print(x)


