from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
import json


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

# query = {"age": {"$gt": 25}}
# result = collection.delete_many(query)
# print("Deleted document count:", result.deleted_count)

query = {
    "$and": [
        {"age": {"$gt": 25}},
        {"email": {"$regex": "@example\.com$"}}
    ]
}
documents = collection.find(query)

for doc in documents:
    print(doc)


# query = {"age": {"$gt": 25}}
# documents = collection.find(query).sort("name", pymongo.ASCENDING)

for doc in documents:
    print(doc)

with open("accounts.json", "r") as file:
    for line in file:
        try:
            data = json.loads(line)  # Charger chaque ligne séparément
            if "account_number" in data:  # Vérifier si c'est une donnée utile
                collection.insert_one(data)
        except json.JSONDecodeError:
            print(f"Erreur lors du parsing de la ligne : {line}")

print("Insertion terminée.")

index_name = "city_index"
collection.create_index("address.city", name=index_name)
print("Index créé.")

city = "Bradshawborough"
results = collection.find({"address.city": city})
min_balance = 30000
for result in results:
    print(result)

results = collection.find({"balance": {"$gt": min_balance}})

for result in results:
    print(result)

pipeline = [
    {"$group": {"_id": "$address.city", "total_balance": {"$sum": "$balance"}}},
    {"$sort": {"total_balance": -1}}
]

results = collection.aggregate(pipeline)

for result in results:
    print(f"{result['_id']}: {result['total_balance']}")



pipeline = [
    {"$match": {"age": {"$gt": 25}}},
    {"$group": {"_id": "$age", "count": {"$sum": 1}}}
]
results = collection.aggregate(pipeline)

for result in results:
    print(result)