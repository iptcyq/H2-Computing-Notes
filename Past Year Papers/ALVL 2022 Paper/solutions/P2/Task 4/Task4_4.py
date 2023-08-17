#Task 4.4 (using <style>)

from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    conn = sqlite3.connect("LIBRARY.db")
    returns = list(conn.execute("SELECT Member.FamilyName, Member.GivenName, Book.Title FROM Book INNER JOIN Loan ON Book.BookID = Loan.BookID INNER JOIN Member ON Member.MemberNumber = Loan.MemberNumber WHERE Loan.Returned = 'FALSE'"))
    # returns is a list, so returns[i] to access
    conn.close()
    return render_template('index.html', loans = returns)
    # using <style> instead of css

if __name__ == '__main__':
    app.run()
