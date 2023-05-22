import pymongo
client = pymongo.MongoClient("127.0.0.1", 27017)
# client.drop_database("supermarket")
db = client.get_database("supermarket")
col = db.get_collection("items")

file = open("supermarket_items.txt")
data = file.read().split("\n")
file.close()

sorted_data = []
for record in data[1:]:
    name, typ, price = record.split(",")
    sorted_data.append({"name":name,"type":typ,"price":float(price)})

col.insert_many(sorted_data)
client.close()
