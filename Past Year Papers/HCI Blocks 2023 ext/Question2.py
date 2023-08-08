from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['post'])
def login():
    userid = request.form['userid']
    password = request.form['password']
    
    connection = sqlite3.connect("social_media.db")
    query = '''SELECT Name, UserID, Password FROM User
                WHERE UserID = ?'''
    res = connection.execute(query,(userid,)).fetchall()
    connection.close()
    
    if len(res) == 0: # no such user
        return "Error: No such user"
    elif res[0][2] != password: # wrong password
        return "Error: Wrong password"
    else: # all correct
        return f"Welcome {res[0][0]}"

if __name__ == "__main__":
    app.run()
