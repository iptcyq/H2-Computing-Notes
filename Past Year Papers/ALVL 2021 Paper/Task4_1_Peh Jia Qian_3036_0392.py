# task 4.1
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roundone')
def roundone():
    return "round 1 results"

@app.route('/roundtwo')
def roundtwo():
    return "round 2 results"

@app.route('/roundthree')
def roundthree():
    return "round 3 results"

@app.route('/mean')
def mean():
    return "mean scores"

@app.route('/qualifiers')
def qualifiers():
    return "qualifier results"

if __name__ == "__main__":
    app.run()

#im damn lazy to continue, maybe another time :)
