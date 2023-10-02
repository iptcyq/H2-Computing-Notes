# Task 2.2
import sqlite3
connection = sqlite3.connect("ServiceLog.db")

class ServiceRecord():
    def __init__(self,Sender,AccessDate,Status,AppType):
        self.Sender = Sender
        self.AccessDate = AccessDate
        self.Status = Status
        self.AppType = AppType

    def isSuccess(self):
        return self.Status == 200
    def getAppType(self):
        return self.AppType

f = open("resource/LOG.txt")
data = f.read().strip()
f.close()

records = data.split("\n")
for rec in records:
    if rec[-1].isalpha(): # differentiate between ip and phone
        sender, date, status, app = rec.split(" ")
        query = '''INSERT INTO
            Log(Sender,AccessDate,Status,AppType)
            VALUES (?,?,?,?)'''
        connection.execute(query, (sender, date, status, app))
    else:
        sender, date, status = rec.split(" ")
        query = '''INSERT INTO
            Log(Sender,AccessDate,Status)
            VALUES (?,?,?)'''
        connection.execute(query, (sender, date, status))
        app = None
    newRecord = ServiceRecord(sender,date,status,app)

connection.commit()
connection.close()
