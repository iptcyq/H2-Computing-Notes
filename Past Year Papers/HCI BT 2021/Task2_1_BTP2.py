# Task 2.1
import pymongo, json
client = pymongo.MongoClient('127.0.0.1', 27017)
client.drop_database("Vaccine")
db = client.get_database("Vaccine")
col = db.get_collection("Staff")

f = open("Materials/Additional_Materials/STAFF.json")
data = json.load(f)
f.close()

col.insert_many(data)
client.close()
