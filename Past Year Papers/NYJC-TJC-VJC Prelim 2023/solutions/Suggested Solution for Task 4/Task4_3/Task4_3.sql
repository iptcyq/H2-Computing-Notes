SELECT "Member"."FirstName", "Member"."LastName", "Member"."Phone", "Course"."Description", "Certificate"."IssueDate"
FROM "Member"
INNER JOIN "Certificate"
	ON "Member"."MemberId" = "Certificate"."MemberId"
INNER JOIN "Course"
	ON "Certificate"."CourseCode" = "Course"."CourseCode"
WHERE "Certificate"."IssueDate" >= '2023-02-01'
ORDER BY "Member"."LastName", "Member"."FirstName" ASC;