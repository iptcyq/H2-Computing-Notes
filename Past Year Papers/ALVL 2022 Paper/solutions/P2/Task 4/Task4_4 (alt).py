#Task 4.4 (with css)

from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    conn = sqlite3.connect("LIBRARY.db")
    returns = list(conn.execute("SELECT Member.FamilyName, Member.GivenName, Book.Title FROM Book INNER JOIN Loan ON Book.BookID = Loan.BookID INNER JOIN Member ON Member.MemberNumber = Loan.MemberNumber WHERE Loan.Returned = 'FALSE'"))
    # returns is a list, so returns[i] to access
    conn.close()
    return render_template('index2.html', loans = returns)
    # index2.html used for css (instead of <style> in html)

if __name__ == '__main__':
    app.run()
