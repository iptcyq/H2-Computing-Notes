import flask, sqlite3
from flask import render_template, url_for


app = flask.Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/<int:round>')
def round_score(round):
    f = open('Task4_2.sql','r')
    query = f.read().strip()
    f.close()
    
    db = sqlite3.connect('Task4.db')
    cur = db.execute(query)
    results = []
    for row in cur:
        results.append(row)
    return render_template('total.html', round = round, results = results)

@app.route('/mean')
def mean_score():
    f = open('Task4_3.sql','r')
    query = f.read().strip()
    f.close()
    
    db = sqlite3.connect('Task4.db')
    cur = db.execute(query)
    results = []
    for row in cur:
        name = row[0]
        score = round(row[1], 2)
        results.append((name, score))
    return render_template('average.html', results = results)
     

@app.route('/qualifiers')
def qualify():
    f = open('Task4_4.sql','r')
    query = f.read().strip()
    f.close()
    
    db = sqlite3.connect('Task4.db')
    cur = db.execute(query)
    results = []
    for row in cur:
        name, score, qBool = row
        if qBool == 1:
            qStr = 'Qualified'
        else:
            qStr = 'Not Qualified'
        results.append([name, score, qStr])
    return render_template('qualification.html', results = results)

if __name__ == '__main__':
    app.run()

