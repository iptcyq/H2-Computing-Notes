# task 3.1
import json
from pymongo import MongoClient

f = open("resource/RENTAL.JSON", 'r')
data = json.load(f)

client = MongoClient("127.0.0.1")

client.drop_database("StyleTheory") # debugging
col = client.get_database("StyleTheory").get_collection("Rental")
col.insert_many(data)

f.close()

# task 3.2
print("Style Theory")
print("Option 1 – Insert new rental")
print("Option 2 – Update existing rental")
print("Option 3 – Quit")
cmd = input("Enter your option (1, 2, or 3): ")

if cmd == '1': # insert new rental
    entry = {}
    
    entry["catalogueNumber"] = input("Enter Catalogue Number: ")
    entry["brand"] = input("Enter brand: ")
    entry["category"] = input("Enter category: ").lower()
    entry["fee"] = int(input("Enter daily rental fee: "))

    if entry["category"] == 'apparel':
        entry["size"] = int(input("Enter size: "))

    entry["email"] = input("Enter email")
    entry["startDate"] = input("Enter start date (YYY-MM-DD): ")
    entry["endDate"] = input("Enter end date (YYY-MM-DD): ")
    
    col.insert_one(entry)

elif cmd == '2': # update existing rental
    catnum = input("Enter Catalogue Number: ")
    # NOT DONE
else: # quit
    pass

res = col.find()
for i in res:
    print(i)

client.close()
