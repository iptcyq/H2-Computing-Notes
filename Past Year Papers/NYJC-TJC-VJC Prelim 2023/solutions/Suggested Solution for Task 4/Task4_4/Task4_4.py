import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)
app.config.update(
    TEMPLATES_AUTO_RELOAD = True
)

# For Task 4.1
@app.route('/')
def index():
    return render_template('index.html')

# For Task 4.2
@app.route('/deletecert')
def delcert():
    query = """
            DELETE FROM "Certificate"
            WHERE "status" = ?
            """

    params = ('404',)

    with sqlite3.connect('Task4.db') as conn:
        cursor = conn.cursor()
        cursor.execute('pragma foreign_keys=on')

        cursor.execute(query, params)
        conn.commit()
        row_count = cursor.rowcount         

        # conn.close() is called automatically

    return render_template('deletecert.html', certs_deleted=row_count)

# For Task 4.3
@app.route('/viprecipient')
def viprecipient():
    query = """
            SELECT "Member"."FirstName", "Member"."LastName", "Member"."Phone", "Course"."Description", "Certificate"."IssueDate"
            FROM "Member"
            INNER JOIN "Certificate"
                ON "Member"."MemberId" = "Certificate"."MemberId"
            INNER JOIN "Course"
                ON "Certificate"."CourseCode" = "Course"."CourseCode"
            WHERE "Certificate"."IssueDate" >= ?
            ORDER BY "Member"."LastName", "Member"."FirstName" ASC;
            """

    params = ('2023-02-01',)

    with sqlite3.connect('Task4.db') as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        cursor.close()
        # conn.close() is called automatically

    return render_template('viprecipient.html', result=result)

# For Task 4.4
@app.route('/addcert')
def addcert():
    return render_template('addcertrecord.html')

@app.route('/result', methods=["POST"])
def status():
    """Display result of the record insertion"""
    success = True

    # Get form data from request
    memberid = request.form['memberid']
    coursecode = request.form['coursecode']
    issuedate = request.form['issuedate']
    status = '200'

    query = """
        INSERT INTO "Certificate"
        ("MemberId", "CourseCode", "IssueDate", "Status")
        VALUES (?, ?, ?, ?)
    """
    params = (memberid, coursecode, issuedate, status)
    
    with sqlite3.connect("Task4.db") as conn:
        cursor = conn.cursor()
        # The following line is needed as the sqlite3 module
        # for Python does not enable foreign key enforcement
        # by default
        cursor.execute('pragma foreign_keys = on')
        try:
            cursor.execute(query, params)
            conn.commit()
        except sqlite3.Error as err:
            print(''.join(err.args))
            success = False
            
        cursor.close()
        # conn.close() is called automatically
    
    result = [memberid, coursecode, issuedate, status, success]
    
    return render_template("result.html", result=result)

app.run()
