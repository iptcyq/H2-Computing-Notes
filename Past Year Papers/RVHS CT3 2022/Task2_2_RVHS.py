import pymongo
client = pymongo.MongoClient("127.0.0.1",27017)
db = client.get_database("supermarket")
col = db.get_collection("items")

def get_cmd():
    print("Choose an option:")
    print("1. Find cost by item name.")
    print("2. Find items by type.")
    print("3. Update cost by item name.")
    print("4. Quit")
    command = int(input("Choose an option:"))
    return command

cmd = get_cmd()
while cmd != 4:
    if cmd == 1:
        item = input("Type an item name:")
        query = {'name':{'$eq':item}}
        cursor = col.find_one(query)
        print(f"{item} each cost ${cursor.get('price')}.")
    elif cmd == 2:
        typ = input("Type an item type:")
        query = {'type':{'$eq':typ}}
        result = col.find(query)
        for count, i in enumerate(result):
            print(f"{count+1} {i['name']}")
    elif cmd == 3:
        item = input("Type an item name you want to update price:")
        cursor = col.find_one({'name':{'$eq':item}})
        if cursor == None:
            print("Error: Item not found.")
        else:
            new_price = float(input("Type a new update price:"))
            search = {'name':{'$eq':item}}
            update = {'$set':{'price':new_price}}
            col.update_one(search, update)
        
    cmd = get_cmd()

client.close()
print("Program quitted.")
