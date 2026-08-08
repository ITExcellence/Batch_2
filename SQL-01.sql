Count the total number of students:

SELECT COUNT(*) AS total_students
FROM students;

Calculate the average age:

SELECT AVG(age) AS average_age
FROM students;


Find the minimum and maximum ages:
SELECT
    MIN(age) AS youngest_age,
    MAX(age) AS oldest_age
FROM students;



SELECT
    department,
    COUNT(*) AS student_count
FROM students
GROUP BY department;


UPDATE students
SET
    age = 22,
    department = 'Software Engineering'
WHERE email = 'amina@example.com';

-- Sort students from youngest to oldest:
SELECT name, age
FROM students
ORDER BY age ASC;

-- Sort students from oldest to youngest:
SELECT name, age
FROM students
ORDER BY age DESC;






SELECT
FROM
WHERE
ROUND
AS
LIKE
IN
BETWEEN
AVG
MIN
MAX
COUNT
ORDER BY ASC DESC


CREATE TABLE
INSERT

ALTER TABLE
RENAME
ADD COLUMN
DROP 
MODIFY
UPDATE
SET
