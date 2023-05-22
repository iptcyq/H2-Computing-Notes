import sqlite3
from flask import Flask, render_template

connection = sqlite3.connect("StoreSG.db")
query = '''SELECT * FROM Product'''
cursor = connection.cursor()
rows = cursor.execute(query).fetchall()

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('Task4_4_index_YIJC.html', products=rows)

@app.route('/form/', methods=["post"])
def form():
    data = request.form
    productid, qty, schoolcode = int(data['id']), int(data['qty']), int(data['schoolcode'])
    query = '''INSERT INTO Buy(SchoolCode, ProductID, Qty, Status)
VALUES(?, ?, ?, ?)'''
    status = "Pending"
    connection.execute(query, (schoolcode, productid, qty, status))
    connection.commit()
##    return render_template('Task4_4_index_YIJC.html', products=com)

if __name__ == '__main__':
    app.run()

connection.close()
