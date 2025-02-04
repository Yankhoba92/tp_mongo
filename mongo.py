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

query = {"name": "John Doe"}
document = collection.find_one(query)
print(document)
query = {"age": {"$gt": 25}}
documents = collection.find(query)

for doc in documents:
    print(doc)

query = {"age": {"$gt": 25}}
update = {"$inc": {"age": 1}}
result = collection.update_many(query, update)
print("Modified document count:", result.modified_count)

query = {"name": "John Doe"}
result = collection.delete_one(query)
print("Deleted document count:", result.deleted_count)