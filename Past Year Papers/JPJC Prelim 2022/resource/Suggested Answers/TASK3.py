import pymongo, json
from datetime import date

#Task 3.1
client = pymongo.MongoClient("127.0.0.1", 27017)
db = client.get_database("StyleTheory")
db.drop_collection("Rental")
coll = db.get_collection("Rental")

with open("RENTAL.JSON") as file:
    data = json.load(file)
    client["StyleTheory"]["Rental"].insert_many(data)

result = coll.find()
for document in result:
    print(document)
    sd = document["startDate"]
    ed = document["endDate"]
    
    f_date = date(int(sd[:4]), int(sd[5:7]), int(sd[8:]))
    l_date = date(int(ed[:4]), int(ed[5:7]), int(ed[8:]))
    delta = l_date - f_date
    print(delta.days)
    print()
    
print()

#Task 3.2
print("""
Style Theory
Option 1 - Insert new rental
Option 2 - Update existing rental
Option 3 - Quit
""")

choice = input("Enter your option (1, 2, or 3): ")

if choice == "1":
    num = int(input("Enter category number: "))
    br = input("Enter brand: ")
    cat = input("Enter A for apparel and B for Bag: ")
    fee = int(input("Enter daily rental fee: "))

    if cat == "A":
        size = int(input("Enter size: "))

    email = input("Enter email: ")
    s_date = input("Enter start date YYYY-MM-DD: ")
    e_date = input("Enter end date YYYY-MM-DD: ")

    if cat == "A":   
        coll.insert_one({"catalogueNumber":num, "brand":br, "category":cat, "rental":fee, "size":size, "email":email, "startDate":s_date, "endDate":e_date})
    else:
        coll.insert_one({"catalogueNumber":num, "brand":br, "category":cat, "rental":fee, "email":email, "startDate":s_date, "endDate":e_date})

elif choice == "2":
    num = int(input("Enter category number: "))
    s_date = input("Enter start date YYYY-MM-DD: ")
    e_date = input("Enter new end date YYYY-MM-DD: ")

    search = {'catalogueNumber':num, "startDate":s_date}
    update = {'$set':{'endDate':e_date}}
    coll.update_one(search, update)
    
print()

client.close()


