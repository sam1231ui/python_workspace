from Bank_app_with_db.app.config.db_and_collection import DataBase

# database connection
client = DataBase("myDatabase")

# define pipleine
# Joining posts with comments and users
pipeline1 = [
    {
        "$lookup": {
            "from": "Comments",
            "localField": "_id",
            "foreignField": "post_id",
            "as": "comments"
        }
    },
    {
        "$lookup": {
            "from": "Users",
            "localField": "user_id",
            "foreignField": "_id",
            "as": "user"
        }
    },
    {
        "$unwind": "$user"
    }
]

pipeline2 = [
    {
        "$lookup": {
            "from": "Posts",
            "localField": "_id",
            "foreignField": "user_id",
            "as": "posts"
        }
    },
    {
        "$unwind": "$posts"
    },
    {
        "$lookup": {
            "from": "Comments",
            "localField": "posts._id",
            "foreignField": "post_id",
            "as": "posts.comments"
        }
    }
]

# Execute the aggregation pipeline
result = client.get_collection("Posts").aggregate(pipeline1)
data = client.get_collection("Users").aggregate(pipeline2)

# Print the result
for post in result:
    print(post)

print("\nThis is data of 2nd pipline")

for data in data:
    print(data)
