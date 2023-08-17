import flask, os, sqlite3
from flask import render_template, request, redirect, url_for

# use for solution that read file
from  Task4_2 import Person
from  Task4_2 import Student
from  Task4_2 import Staff

app = flask.Flask(__name__)

#class to be used for displaying the information on the webpage
#identity value is derived
    
class PersonRec():
    def __init__(self, fullname, screenname, isadult):
        self._fullname = fullname
        self._screenname = screenname
        self._isadult = isadult
        if self._isadult:
            if self._screenname.endswith('Staff'):
                self._identity ='Staff'
            else:
                self._identity ='People'
        else:
            self._identity ='Student'

    def fullname(self):
        return self._fullname

    def screenname(self):
        return self._screenname

    def identity(self):
        return self._identity
    
    def setIdentity(self, identity):
        self._identity=identity

    def getFullName(self):
        return self._fullname

    def screen_name(self):
        return self._screenname
    
#this solution draw data from database but need to use PersonRec setIdentity method to derive
#the identity of the record

@app.route('/db', methods=['GET'])
def index():
    db = sqlite3.connect('school.db')
    #db.row_factory = sqlite3.Row
    cursor = db.execute('SELECT fullname, screenname, IsAdult FROM People ')
    all_rows = cursor.fetchall()
    cursor.close()
    db.close()
    listx=[]
    for row in all_rows:
        r=PersonRec(row[0], row[1], row[2])
        listx.append(r)
        
    return render_template('index.html', results=listx)
    
#this solution get data from the text file and uses the classes in Task4_2 with added methods 
#to provide the value of the identity of the record

@app.route('/', methods=['GET'])
def index2():
    listx=[]
    with open("People.txt","r") as fobj:
        line = fobj.readline()
        while line !='':
            record=line.split(",")
            if record[2].strip()=='Person':
                p=Person(record[0], record[1])
            elif record[2].strip()=='Staff':
                p=Staff(record[0], record[1])
            else:
                p=Student(record[0], record[1])
            listx.append(p)
            line = fobj.readline()
    return render_template('index.html', results=listx)

if __name__ == '__main__':
    app.run()        
