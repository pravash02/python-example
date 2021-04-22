 CREATE TABLE console.user_details (
   EmployeeNo INTEGER,
   FirstName VARCHAR(30),
   LastName VARCHAR(30),
   DOB DATE FORMAT 'YYYY-MM-DD',
   JoinedDate DATE FORMAT 'YYYY-MM-DD',
   DepartmentNo BYTEINT
)
UNIQUE PRIMARY INDEX ( EmployeeNo );

INSERT INTO console.user_details (
   EmployeeNo,
   FirstName,
   LastName,
   DOB,
   JoinedDate,
   DepartmentNo
)
VALUES (
   101,
   'Mike',
   'James',
   '1980-01-05',
   '2005-03-27',
   01
);

SELECT TableName
FROM DBC.TablesV
WHERE DatabaseName = 'console';