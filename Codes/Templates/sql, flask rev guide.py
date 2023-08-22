# sql
import sqlite3

conn = sqlite3.connect('db.db') # db name
conn.execute('sql')
conn.execute('... VALUES(?, ?)', (value1, value2))

conn.commit()
conn.close()


# flask
import flask

app = flask.Flask(__name__)

@app.route('/', methods = ['GET']) # '/' for main webpage 
def index():
    return flask.rendere_template('index.html') # whatever is the name of the html file

@app.route('/second', methods = ['GET', 'POST']) # 'POST' for forms
def second():
    if flask.request.method == 'GET':
        return flask.render_template('second.html')
    if 'action' in flask.request.form:
        action = flask.request.form['action']
        var = flask.request.form['var']
        # ...
    if action == 'submit' # name of button
        # insert into db or something
    return flask.render_template('second.html') # or something else if u wanna return to home page

@app.route('/third', methods = ['GET'])
def third():
    conn = sqlite3.connect('db.db')

    query  = 'some sql'
    
    cursor = conn.execute(query)
    allrows = cursor.fetchall()

    # convert return into array
    ret = []
    for row in allrows:
        ret.append(row)

    return flask.render_template('third.html', table = ret) # use var table in html

if __name__ == '__main__': # actl makes your damn app run 
    app.run()
