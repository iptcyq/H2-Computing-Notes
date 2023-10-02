import sqlite3

f = open("../resource/books_data.txt")
books = f.read().strip().split("\n")
f.close()

f = open("../resource/copies_data.txt")
copies = f.read().strip().split("\n")
f.close()

conn = sqlite3.connect("../resource/Task4.db")

for book in books:
    bookID, title, price = book.split(",")
    conn.execute('''INSERT INTO books(bookID, title, price)
    VALUES(?,?,?)''', (bookID, title, price))

for copy in copies:
    copyID, bookID, title, price = copy.split(",")
    conn.execute('''INSERT INTO copies(copyID, bookID)
    VALUES(?,?)''', (copyID, bookID))

conn.commit()
conn.close()
