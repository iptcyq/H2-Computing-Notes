SELECT Member.Name, Member.Gender, Member.Age, 
FitnessRecord.Weight, FitnessRecord.Height, 
FitnessRecord.WorkoutDate FROM Member
LEFT JOIN FitnessRecord 
ON Member.MemberID = FitnessRecord.MemberID
ORDER BY Member.Gender ASC, Member.Name ASC

SELECT COUNT(*), AVG(Member.Age), 
AVG(FitnessRecord.Weight), AVG(FitnessRecord.Height)
FROM Member INNER JOIN FitnessRecord 
ON Member.MemberID = FitnessRecord.MemberID
GROUP BY FitnessRecord.WorkoutDate