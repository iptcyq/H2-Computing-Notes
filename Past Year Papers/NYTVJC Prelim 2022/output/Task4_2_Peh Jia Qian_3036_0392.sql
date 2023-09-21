SELECT Person.Name, Record.Time FROM Person 
INNER JOIN Record on Person.id = Record.id 
WHERE Person.Role = 'Student' 
 Record.Time > '0730' 
AND Record.Type = 'entry'
ORDER BY Record.Date, Record.Time ASC