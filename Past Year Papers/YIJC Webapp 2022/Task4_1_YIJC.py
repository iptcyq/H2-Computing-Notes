import sqlite3

connection = sqlite3.connect("StoreSG.db")
query = '''
CREATE TABLE `Buy` (
    `BuyID`	INTEGER PRIMARY KEY AUTOINCREMENT,
    `SchoolCode`INTEGER,
    `ProductID`	INTEGER,
    `Qty`	INTEGER,
    `Status`    TEXT,
    FOREIGN KEY(`ProductID`) REFERENCES `Product`(`ProductID`),
    FOREIGN KEY(`SchoolCode`) REFERENCES `School`(`SchoolCode`)
);'''
connection.execute(query)

file = open("Buy.TXT")
data = file.read()
file.close()
rows = data.split("\n")
rows = rows[1:-1]
for row in rows:
    values = row.split(",")
    schoolcode, productid, qty, status = values
    query = '''INSERT INTO Buy(SchoolCode, ProductID, Qty, Status)
VALUES(?, ?, ?, ?)'''
    connection.execute(query,(schoolcode, productid, qty, status))
connection.commit()
connection.close()
    
