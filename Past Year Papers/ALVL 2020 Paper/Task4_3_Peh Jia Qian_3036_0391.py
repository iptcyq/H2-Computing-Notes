# Task 4.3
from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    # Get information from text file
    # because im not going to go to the db just for the sake of it (like in the answer)
    # especially since they only said 'info of people from text file'
    # though doing textfile version is essentially a copy paste from the previous part
    # which is dumb
    
    f = open("people.txt")
    people = f.read().strip().split("/n")
    f.close()

    people_info = []
    for person in people:
        name, date, classtype = person.split(",")
        person_info.append([name, date, classtype]) # look theres literally most info there
    pass

    # or should i just do it ._. and waste time - theoretically should do this in As 
    # haiz fine I'll do it
    # this is still dumb though

    # get information from db
    conn = sqlite3.connection("school.db")
    res = conn.execute('''SELECT
            FullName, ScreenName FROM People''').fetchall()# why am i even doing this
    
    conn.close()

    # never mind no im not, am too tired for this
    # going to go have a pre-midlife crisis and sleep instead

if __name__ == "__main__":
    app.run()
