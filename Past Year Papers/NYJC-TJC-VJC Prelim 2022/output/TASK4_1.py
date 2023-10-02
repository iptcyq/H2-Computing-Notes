from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/latecomers')
def latecomers():
    conn = sqlite3.connect('../resource/Task4.db')

    query = '''
    SELECT Person.Name, Record.Time FROM Person 
    INNER JOIN Record on Person.id = Record.visitorId
    WHERE Person.Role = 'Student' AND Record.Time > '0730'
    AND Record.Type = 'entry'
    ORDER BY Record.Date, Record.Time ASC'''
    result = conn.execute(query).fetchall()

    conn.close()
    return render_template('latecomers.html', result=result)

@app.route('/addrecord')
def addrecord():
    return render_template('addrecord.html')

@app.route('/submitrecord', methods=["POST"])
def submitrecord():
    userid, direction = request.form["ID"], request.form["dir"]
    conn = sqlite3.connect('../resource/Task4.db')

    # validate userid and direction
    query = '''
    SELECT * FROM Person WHERE Person.id = ?'''
    result = conn.execute(query, (userid,)).fetchall()
    if len(result) == 0: # id does not exist
        conn.close()
        return "Error: User ID does not exist"
    elif direction != "entry" and direction != "entry":
        conn.close()
        return "Error: Invalid direction"
    else:
        query = '''
        INSERT INTO Record(Date, Time, Type, visitorID)
        VALUES('2022-10-05', '0722', ?, ?)'''
        conn.execute(query, (userid, direction))
        conn.commit()
    
    conn.close()
    return "Success! Record added."

if __name__ == "__main__":
    app.run()
