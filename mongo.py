from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')


db = client.mydb
collection = db.mycollection

documents = [
    {"name": "Alice", "email": "alice@example.com", "age": 25},
    {"name": "Bob", "email": "bob@example.com", "age": 35}
]
result = collection.insert_many(documents)
print("Inserted document IDs:", result.inserted_ids)