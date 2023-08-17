from sqlite3 import *

conn = connect("JPFashion.db")
#conn.execute("DROP table Customer;")
#conn.execute("DROP table Product;")
#conn.execute("DROP table CustomerRental;")
#conn.execute("DROP table ProductRental;")


file = open("CUSTOMER.TXT",'r')
file.readline() #skip header

for line in file:
    line = line.strip()
    Email,FirstName,LastName,ContactNumber,DOB,Address = line.split(',')
    conn.execute("insert into Customer values (?,?,?,?,?,?)", (Email,FirstName,LastName,ContactNumber,DOB,Address))
    conn.commit()

file.close()

file = open("PRODUCT.TXT",'r')
file.readline() #skip header

for line in file:
    line = line.strip()
    CatalogueNumber,Category,Brand,Size,Fee = line.split(',')
    conn.execute("insert into Product values (?,?,?,?,?)", (CatalogueNumber,Category,Brand,Size,Fee))
    conn.commit()

file.close()

file = open("CUSTOMERRENTAL.TXT",'r')
file.readline() #skip header

for line in file:
    line = line.strip()
    ID,Email,StartDate,EndDate = line.split(',')
    conn.execute("insert into CustomerRental values (?,?,?,?)", (ID,Email,StartDate,EndDate))
    conn.commit()

file.close()

file = open("PRODUCTRENTAL.TXT",'r')
file.readline() #skip header

for line in file:
    line = line.strip()
    ID,CatalogueNumber,Returned = line.split(',')
    conn.execute("insert into ProductRental values (?,?,?)", (ID,CatalogueNumber,Returned))
    conn.commit()

file.close()

conn.close()
