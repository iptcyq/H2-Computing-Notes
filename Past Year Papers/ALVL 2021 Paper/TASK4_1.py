
# task 4.1
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roundone')
def roundone():
    conn = sqlite3.connect("resource/Task4.db")

    query = '''SELECT competitor.name, scores.score 
            FROM competitor INNER JOIN scores 
            ON competitor.id = scores.id 
            WHERE scores.round = 1 
            ORDER BY scores.score DESC'''
    results = conn.execute(query).fetchall()
    
    conn.close()
    return render_template('roundone.html', results=results)

@app.route('/roundtwo')
def roundtwo():
    conn = sqlite3.connect("resource/Task4.db")

    query = '''SELECT competitor.name, scores.score 
            FROM competitor INNER JOIN scores 
            ON competitor.id = scores.id 
            WHERE scores.round = 2 
            ORDER BY scores.score DESC'''
    results = conn.execute(query).fetchall()
    
    conn.close()
    return render_template('roundone.html', results=results)

@app.route('/roundthree')
def roundthree():
    conn = sqlite3.connect("resource/Task4.db")

    query = '''SELECT competitor.name, scores.score 
            FROM competitor INNER JOIN scores 
            ON competitor.id = scores.id 
            WHERE scores.round = 3 
            ORDER BY scores.score DESC'''
    results = conn.execute(query).fetchall()
    
    conn.close()
    return render_template('roundone.html', results=results)

@app.route('/mean')
def mean():
    conn = sqlite3.connect("resource/Task4.db")

    query = '''SELECT competitor.name, AVG(scores.score)
            FROM scores
            INNER JOIN competitor on competitor.id = scores.id
            GROUP BY scores.id
            ORDER BY competitor.name'''
    results = conn.execute(query).fetchall()
    
    conn.close()
    return render_template('roundone.html', results=results)

@app.route('/qualifiers')
def qualifiers():
    return "qualifier results"

if __name__ == "__main__":
    app.run()

#im damn lazy to continue, maybe another time :)
