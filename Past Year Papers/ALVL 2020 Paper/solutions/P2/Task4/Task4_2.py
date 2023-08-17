from datetime import date
#import re
import sqlite3

class Person:
    def __init__(self, fullName, dateOfBirth):
        self._full_name = fullName
        self._date_of_birth = dateOfBirth

    def getFullName(self):
        return self._full_name
    
    def getDateofBirth(self):
        return self._date_of_birth
    
    def is_adult(self):
        dobYear = int(self._date_of_birth[0:4])
        currentYear = int(date.today().year)
        if currentYear - dobYear > 18:
            return True
        else:
            return False
        
    def screen_name(self):
        name = ''
        #name = re.sub(r'[^\w\s]','',self._full_name).replace(' ','')
        for c in self._full_name:
            if (ord(c)>=65 and ord(c)<=90) or (ord(c)>=97 and ord(c)<=122):
                 name+=c               
        monthday = self._date_of_birth[5:].replace('-','')
        return name+monthday
    
    #Added to provide value for identity
    def identity(self):
        return "Person"

class Staff(Person):
    def __init__(self,fullName, dateOfBirth):
        super().__init__(fullName, dateOfBirth)

    def is_adult(self):
        return True
        
    def screen_name(self):
        return self._full_name + "Staff"
    
    #Added to provide value for identity
    def identity(self):
        return "Staff"

class Student(Person):
    def __init__(self,fullName, dateOfBirth):
        super().__init__(fullName, dateOfBirth)

    def is_adult(self):
        return False

    #Added to provide value for identity
    def identity(self):
        return "Student"
    



#method to insert data into People table       
def insertPerson(person):
    connection = sqlite3.connect("school.db")
    connection.execute("INSERT INTO People(FullName,DateOfBirth, ScreenName,IsAdult) VALUES (?,?,?,?)", (person.getFullName(), person.getDateofBirth(), person.screen_name(), person.is_adult()))
    connection.commit()
    connection.close()
    
def main():
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
            insertPerson(p)
            line = fobj.readline()
        
main()

#p = Student("Tan Ah Seng","1972-11-30")
#print(p.screen_name())
#print(p.is_adult())
