from flask import Flask, render_template, request
app = Flask(__name__)
import sqlite3
connection = sqlite3.connect('resource/students.db')

def cursor_to_list(cursor):
    ret = []
    for doc in cursor:
        ret.append(doc)
    return ret

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/student_rec')
def student_rec():
    query = '''SELECT Student.Name, Student.Gender, 
            StudentHealthRecord.Weight,
            StudentHealthRecord.Height 
            FROM Student LEFT JOIN StudentHealthRecord 
            ON Student.StudentID = StudentHealthRecord.StudentID
            ORDER BY Student.Gender ASC, Student.Name DESC'''
    results = cursor_to_list(connection.execute(query))
    return render_template('StudentRec.html', results=results)

@app.route('/health_rec')
def health_rec():
    results = []
    results.append(cursor_to_list(connection.execute('''
    SELECT COUNT(StudentID)FROM Student
    WHERE Student.Gender = 'M' ''')))
    results.append(cursor_to_list(connection.execute('''
    SELECT COUNT(StudentID)FROM Student
    WHERE Student.Gender = 'F' ''')))
    results.append(cursor_to_list(connection.execute(''' SELECT
    AVG(StudentHealthRecord.Weight) FROM Student
    INNER JOIN StudentHealthRecord ON Student.StudentID
    = StudentHealthRecord.StudentID WHERE Student.Gender = 'M' ''')))
    results.append(cursor_to_list(connection.execute(''' SELECT
    AVG(StudentHealthRecord.Weight) FROM Student
    INNER JOIN StudentHealthRecord ON Student.StudentID
    = StudentHealthRecord.StudentID WHERE Student.Gender = 'F' ''')))
    results.append(cursor_to_list(connection.execute(''' SELECT
    AVG(StudentHealthRecord.Height) FROM Student
    INNER JOIN StudentHealthRecord ON Student.StudentID
    = StudentHealthRecord.StudentID WHERE Student.Gender = 'M' ''')))
    results.append(cursor_to_list(connection.execute(''' SELECT
    AVG(StudentHealthRecord.Height) FROM Student
    INNER JOIN StudentHealthRecord ON Student.StudentID
    = StudentHealthRecord.StudentID WHERE Student.Gender = 'F' ''')))
    return render_template('HealthRec.html', results=results)

@app.route('/add_rec')
def add_rec():
    return render_template('AddRec.html')

@app.route('/submit', methods=["post"])
def submit():
    data = request.form
    query = '''INSERT INTO Student(StudentID, Name, Gender) VALUES (?,?,?)'''
    connection.execute(query,(int(data["StudentID"]),data["Name"],data["Gender"]))
    query = '''INSERT INTO StudentHealthRecord(StudentID, Weight, Height) VALUES (?,?,?)'''
    connection.execute(query,(int(data["StudentID"]),float(data["Weight"]),float(data["Height"])))
    connection.commit()
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

connection.close()
