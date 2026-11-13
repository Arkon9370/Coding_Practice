-- Create a new database
CREATE DATABASE CompanyDB;
-- Use that database
USE CompanyDB;
-- Create a table
CREATE TABLE Person (
    id INT PRIMARY KEY,
    email VARCHAR(50) NOT NULL
);
-- Insert data
INSERT INTO Person (id, email) 
VALUES 
(1, 'a@b.com'),
(2, 'c@d.com'),
(3, 'a@b.com ');
-- Write the Answer
SELECT email 
FROM Person 
GROUP BY email 
HAVING COUNT(email) > 1;
-- (EXTRA) To Delete the Duplicates
DELETE p1
FROM Person p1
JOIN Person p2
ON p1.email = p2.email
AND p1.id > p2.id;
-- For tables alias we may not use AS but For columns alias its a must