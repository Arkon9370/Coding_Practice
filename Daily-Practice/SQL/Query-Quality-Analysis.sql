-- Create a new database
CREATE DATABASE CompanyDB;
-- Use that database
USE CompanyDB;
-- Create a table
CREATE TABLE Queries(
    query_name varchar(50),
    result varchar(50),
    position int,
    rating int
);
-- Insert data
INSERT INTO Queries(query_name, result, position, rating) 
VALUES 
('Dog','Golden Retriever',1,5),
('Dog','German Shepherd',2,5),
('Dog','Mule',200,1),
('Cat','Shirazi',5,2),
('Cat','Siamese',3,3),
('Cat','Sphynx',7,4);
-- Write the Answer
SELECT query_name,
round(avg(rating/position),2) as quality,
round(avg(if(rating<3,1,0) * 100),2) as poor_query_percentage
from Queries 
where query_name is not null
group by query_name;