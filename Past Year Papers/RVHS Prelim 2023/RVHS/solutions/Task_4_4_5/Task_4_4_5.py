from flask import Flask, render_template, request, url_for
import sqlite3
from sqlite3 import Error

app = Flask(__name__)

def db_connect(filename):
    try:
        conn = sqlite3.connect(filename)
        return conn
    except Error as e:
        print(e)
        
def pri_sch_summary(conn):
    sql = '''
          SELECT primary_sch, count(*)/4 as 'no of student', round(sum(al)*1.0/count(*)*4,2) as 'mean overall AL' FROM results
              JOIN students
              ON results.student_id = students.student_id
              GROUP by primary_sch;
          '''
    cur = conn.execute(sql)
    rows = cur.fetchall()
    return list(rows)

def get_students(conn, cutoff):
    
    sql = '''SELECT stu_name, gender, primary_sch, sum(al) as overall_al, guardian_name, guardian_email FROM results
                 LEFT JOIN students
                     ON students.student_id = results.student_id
                 LEFT JOIN guardians
                     ON students.guardian_id = guardians.guardian_id
                 GROUP BY results.student_id
                 HAVING overall_al < ?
                 ORDER BY primary_sch DESC, overall_al ASC
          '''
    cur = conn.execute(sql,(cutoff,))
    rows = cur.fetchall()
    return list(rows)
    
@app.route('/')
def index():
    db_conn = db_connect("ENROLMENT.db")
    sch_summary = pri_sch_summary(db_conn)
    db_conn.close()
    return render_template('index.html', sch_summary = sch_summary)

@app.route('/display/', methods = ['POST', 'GET'])
def display():
    if request.method == 'POST':
        cutoff = int(request.form['cutoff'])
        db_conn = db_connect("ENROLMENT.db")
        stu_list = get_students(db_conn, cutoff)
        db_conn.close()
        return render_template('display.html', stu_details = stu_list)
    else:
        return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=False)
