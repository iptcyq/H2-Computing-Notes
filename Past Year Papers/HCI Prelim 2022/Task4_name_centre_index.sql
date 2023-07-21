SELECT Student.Name, Student.Gender, 
StudentHealthRecord.Weight, StudentHealthRecord.Height 
FROM Student LEFT JOIN StudentHealthRecord 
ON Student.StudentID = StudentHealthRecord.StudentID
ORDER BY Student.Gender ASC, Student.Name DESC

SELECT COUNT(StudentID) FROM Student WHERE Student.Gender = 'M' 
SELECT COUNT(StudentID) FROM Student WHERE Student.Gender = 'F' 

SELECT AVG(StudentHealthRecord.Weight) 
FROM Student.StudentID INNER JOIN StudentHealthRecord.StudentID
WHERE Student.Gender = 'M'

SELECT AVG(StudentHealthRecord.Weight) 
FROM Student.StudentID INNER JOIN StudentHealthRecord.StudentID
WHERE Student.Gender = 'F'

SELECT AVG(StudentHealthRecord.Height) 
FROM Student.StudentID INNER JOIN StudentHealthRecord.StudentID
WHERE Student.Gender = 'M'

SELECT AVG(StudentHealthRecord.Height) 
FROM Student.StudentID INNER JOIN StudentHealthRecord.StudentID
WHERE Student.Gender = 'F'

INSERT INTO Student(StudentID, Name, Gender) VALUES (12,'Helen','F')
INSERT INTO StudentHealthRecord(StudentID, Weight, Height) 
VALUES (12,48.7,1.72)