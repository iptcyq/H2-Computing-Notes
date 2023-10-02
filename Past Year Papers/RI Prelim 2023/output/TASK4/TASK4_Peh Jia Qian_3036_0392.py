from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("FITNESS.db")
conn.close()
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/details')
def details():
    conn = sqlite3.connect("FITNESS.db")

    query = '''SELECT Member.Name, Member.Gender, Member.Age, 
            FitnessRecord.Weight, FitnessRecord.Height, 
            FitnessRecord.WorkoutDate FROM Member
            LEFT JOIN FitnessRecord 
            ON Member.MemberID = FitnessRecord.MemberID
            ORDER BY Member.Gender, Member.Name ASC'''
    result = conn.execute(query).fetchall()
    
    conn.close()

    return render_template('details.html',result=result)

@app.route('/statistics')
def statistics():
    conn = sqlite3.connect("FITNESS.db")

    query = '''SELECT COUNT(*), AVG(Member.Age), 
            AVG(FitnessRecord.Weight), AVG(FitnessRecord.Height),
            FitnessRecord.WorkoutDate
            FROM Member INNER JOIN FitnessRecord 
            ON Member.MemberID = FitnessRecord.MemberID
            GROUP BY FitnessRecord.WorkoutDate'''
    data = conn.execute(query).fetchall()

    result = []
    for item in data:
        result.append([item[0], round(item[1],1), \
                      round(item[2],1), round(item[3],1),\
                        item[4]])

    conn.close()
    return render_template('statistics.html',result=result)

@app.route('/addrecord', methods=["POST","GET"])
def addrecord():
    if request.method == "GET":
        return render_template('addrecord.html')
    else: # post
        memberid, weight, height, date = \
        request.form["memberid"], request.form["weight"],\
        request.form["height"], request.form["date"]

        conn = sqlite3.connect("FITNESS.db")
        query = '''INSERT INTO FitnessRecord(MemberID, Weight,
                Height, WorkoutDate) VALUES(?,?,?,?)'''
        conn.execute(query, (memberid, weight, height, date))
        # WRONG - should convert weight, height into float
        conn.commit()
        
        conn.close()
        return "success"

if __name__ == "__main__":
    app.run()
