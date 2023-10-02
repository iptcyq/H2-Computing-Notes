from flask import Flask, render_template
import sqlite3

conn = sqlite3.connect("LIBRARY.db")
conn.close()

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect("LIBRARY.db")

    query = '''SELECT Member.FamilyName, Member.GivenName,
            Book.Title FROM Loan
            INNER JOIN Member ON Loan.MemberNumber = Member.MemberNumber
            INNER JOIN Book ON Loan.BookID = Book.BookID
            WHERE Loan.Returned = 'FALSE' '''
    results = conn.execute(query).fetchall()
    
    conn.close()
    return render_template('index.html', results=results)

if __name__ == "__main__":
    app.run()
