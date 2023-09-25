from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insertbook', methods=["GET","POST"])
def insertbook():
    if request.method == "POST":
        conn = sqlite3.connect("../resource/Task4.db")
        
        bookID, title, price, copies = request.form["bookid"], request.form["title"], request.form["price"], request.form["copies"]
        print(bookID, title, price, copies)

        query = '''INSERT INTO books(bookID, title, price)
        VALUES(?,?,?)'''
        conn.execute(query, (bookID, title, price))

        for i in range(int(copies)):
            copyID = "0"*(4-len(str(i))) + str(i)
            print(copyID)

        query = '''INSERT INTO copies(copyID, bookID)
        VALUES(?,?)'''
        conn.execute(query, (copyID, bookID))

        conn.commit()
        conn.close()
        return "Complete."

    else: # method = GET
        return render_template("insertbook.html")

@app.route('/displaybooks')
def displaybooks():
    conn = sqlite3.connect("../resource/Task4.db")

    query = '''SELECT books.bookID, books.title, books.price,
        COUNT(copies.copyID) FROM books
        INNER JOIN copies ON books.bookID = copies.bookID
        GROUP BY copies.bookID ORDER BY books.title ASC'''
    result = conn.execute(query).fetchall()
    conn.close()
    
    return render_template("displaybooks.html",result=result)

if __name__ == "__main__":
    app.run()
