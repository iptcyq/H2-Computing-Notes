import sqlite3

connection = sqlite3.connect("StoreSG.db")
query = '''
SELECT Product.ProductName, Buy.Qty, Product.UnitCost FROM Buy
INNER JOIN Product ON Product.ProductID=Buy.ProductID
WHERE Buy.SchoolCode=7612'''
cursor = connection.cursor()
rows = cursor.execute(query).fetchall()
totalprice = 0
for row in rows:
    name, qty, cost = row
    print(f"Bought {qty} {name} at ${cost} each")
    totalprice += cost*qty
print(f"Total cost is ${totalprice}")

connection.close()
