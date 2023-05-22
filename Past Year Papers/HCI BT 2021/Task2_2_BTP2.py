# Task 2.2
import pymongo
client = pymongo.MongoClient('127.0.0.1',27017)
db = client.get_database("Vaccine")
col = db.get_collection("Staff")

print("Name, Age, Reason for not accepting vaccine")
query = {"Acceptance":"No"}
results = col.find(query)
for i in results:
    print(f"{i['Name']} of age {i['Age']}: {i['Reason']}")
print()

print("Number of staff with at least one dose")
query = {"VacDates":{"$exists":True}}
results = col.count(query)
print(results)
print()

print("Add Charlie Lee's second dose")
search = {"Name":"Charlie Lee"}
result = col.find(search)
current = [result[0]["VacDates"]]
current.append(("5 Apr 2021"))
update = {"$set":{"VacDates":current}}
col.update_one(search, update)
print()

print("Display name(s) of those at least 50 and with both doses")
query = {"$and":[{"Age":{"$gte":50}},{"VacDates":{"$size":2}}]}
result = col.find(query)
for i in result:
    print(i)

client.close()
