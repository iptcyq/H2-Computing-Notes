# Task 2.4
from flask import Flask, render_template
import sqlite3
from Task2_3_name_centre_index import AppServiceRecord, SmsServiceRecord

connection = sqlite3.connect("ServiceLog.db")
app = Flask(__name__)

@app.route('/')
def index():
    data = []
    
    query = '''SELECT Sender, AccessDate, AppType, Status
            FROM Log'''
    results = connection.execute(query)
    
    for doc in results:
        sender, date, apptype, status = doc
        if apptype == None:
            rec = SmsServiceRecord(sender, date, status)
        else:
            rec = AppServiceRecord(sender, date, status, apptype)

        data.append([sender,date,rec.getAppType(),rec.getSuccess()])
    return render_template("index.html", logs = data)

if __name__ == '__main__':
    app.run()
