import sqlite3

f = open("../resource/CAKES.TXT", 'r')
cakes = f.read().strip().split("\n")
f.close()
f = open("../resource/LOAVES.TXT", 'r')
loaves = f.read().strip().split("\n")
f.close()
f = open("../resource/BUNS.TXT", 'r')
buns = f.read().strip().split("\n")
f.close()

connection = sqlite3.connect("bakery.db")

for cake in cakes:
    ProductCode, Name, Location, Price, ServingSize, Shape = cake.split(",")
    query = '''INSERT INTO
    Product(ProductCode,Name,Type,Location,Price)
    VALUES (?,?,?,?,?)'''
    connection.execute(query,(ProductCode,Name,"Cake",Location,float(Price)))

    query = ''' INSERT INTO
    Cake(ProductCode, ServingSize, Shape)
    VALUES (?,?,?)'''
    connection.execute(query,(ProductCode,int(ServingSize),Shape))

for loaf in loaves:
    ProductCode, Name, Location, Price, Weight = loaf.split(",")
    query = '''INSERT INTO
    Product(ProductCode,Name,Type,Location,Price)
    VALUES (?,?,?,?,?)'''
    connection.execute(query,(ProductCode,Name,"Loaf",Location,float(Price)))

    query = ''' INSERT INTO
    Loaf(ProductCode, Weight)
    VALUES (?,?)'''
    connection.execute(query,(ProductCode,float(Weight)))

for bun in buns:
    ProductCode, Name, Location, Price, PiecesPerPackage = bun.split(",")
    query = '''INSERT INTO
    Product(ProductCode,Name,Type,Location,Price)
    VALUES (?,?,?,?,?)'''
    connection.execute(query,(ProductCode,Name,"Bun",Location,float(Price)))

    query = ''' INSERT INTO
    Bun(ProductCode, PiecesPerPackage)
    VALUES (?,?)'''
    connection.execute(query,(ProductCode,int(PiecesPerPackage)))

connection.commit()
connection.close()
