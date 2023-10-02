# Task 4.2
from datetime import date
import sqlite3

class Person:
    def __init__(self, fullname, birthdate="YYYY-MM-DD"):
        self.full_name = fullname
        # the dumb paper spelled date wrong - im correcting it
        self.date_of_birth = birthdate

    def is_adult(self):
        curr_year = date.today().year
        return curr_year - int(self.date_of_birth[:4]) > 18

    def screen_name(self):
        # they didnt put .replace() in quick ref so haiz
        screenName = ""
        for char in self.full_name:
            if char.isalnum():
                screenName += char
        screenName += self.date_of_birth[5:7]
        screenName += self.date_of_birth[8:10]
        return screenName

class Staff(Person):
    def __init__(self, full_name, birthdate="YYYY-MM-DD"):
        super().__init__(full_name, birthdate)

    def screen_name(self):
        return super().screen_name() + "Staff"
    def is_adult(self):
        return True

class Student(Person):
    def __init__(self, full_name, birthdate="YYYY-MM-DD"):
        super().__init__(full_name, birthdate)

    def is_adult(self):
        return False

f = open("resource/people.txt")
people = f.read().strip().split("\n")
f.close()

everyone = []
for person in people:
    name, birthdate, classtype = person.split(",")

    if classtype == "Person":
        p = Person(name, birthdate)
    elif classtype == "Staff":
        p = Staff(name, birthdate)
    elif classtype == "Student":
        p = Student(name, birthdate)
    everyone.append(p)

conn = sqlite3.connect("school.db")

for p in everyone:
    query = '''INSERT INTO
            People(FullName,DateOfBirth,ScreenName,IsAdult)
            VALUES (?,?,?,?)'''

    isadult = 0
    if p.is_adult():
        isadult = 1
    conn.execute(query,(p.full_name,p.date_of_birth,p.screen_name(),isadult))

conn.commit()
conn.close()
