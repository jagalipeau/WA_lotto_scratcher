import pymongo
import main
import json

# Connect to MongoDB


def update(new_data):
    client = pymongo.MongoClient("mongodb://mongoadmin:pass@localhost:27017/")

    database = client["Wa_Lotto"]

    collection = database["full_data"]
    try:
        collection.insert_many(new_data)
        print("successful")
    except:
        print("failed")

    return None


# Call the update function with the fake car data
# update(database, main.get_data())
