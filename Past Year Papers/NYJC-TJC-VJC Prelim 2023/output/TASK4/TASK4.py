from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/deletecerts')
def deletecerts():
    conn = sqlite3.connect("Task4.db")

    query = '''SELECT COUNT(*) FROM Certificate
            WHERE Status = 404'''
    result = conn.execute(query).fetchall()
    query = '''DELETE FROM Certificate WHERE Status = 404'''
    conn.execute(query)

    conn.close()
    return f"{result} records were removed"

@app.route('/voucher')
def voucher():
    conn = sqlite3.connect("Task4.db")

    query = '''SELECT Member.FirstName, Member.LastName,
            Member.Phone, Course.Description,
            Certificate.IssueDate
            FROM Certificate INNER JOIN Course
            ON Course.CourseCode = Certificate.CourseCode
            INNER JOIN Member
            ON Member.MemberId = Certificate.MemberId
            WHERE NOT Certificate.IssueDate = '2022-01-%'
            ORDER BY Member.LastName ASC, Member.FirstName ASC'''
    result = conn.execute(query).fetchall()

    conn.close()
    return render_template('voucher.html',result=result)

@app.route('/addcert', methods=["GET","POST"])
def addcert():
    if request.method == "GET":
        return render_template('addcert.html')
    else: # POST method
        memberid, code, date = request.form["memberid"], \
                               request.form["coursecode"],\
                               request.form["issuedate"]

        conn = sqlite3.connect("Task4.db")
        
        # check if member id exists
        query = '''SELECT * FROM Member WHERE MemberId = ?'''
        result = conn.execute(query, (int(memberid),)).fetchall()
        if len(result) == 0:
            return f"Error: MemberId<{memberid}> does not exist"

        # check course code exists
        query = '''SELECT * FROM Course WHERE CourseCode = ?'''
        result = conn.execute(query, (code,)).fetchall()
        if len(result) == 0:
            return f"Error: CourseCode<{code}> does not exist"

        # store the record
        query = '''INSERT INTO Certificate(MemberId, CourseCode,
                IssueDate, Status) VALUES(?,?,?,200)'''
        conn.execute(query, (int(memberid), code, date))
        #conn.commit()
        
        conn.close()
        return f"Success. Inserted <Member Id:{memberid}, \
Course Code:{code}, Issue Date:{date}>"

if __name__ == "__main__":
    app.run()
