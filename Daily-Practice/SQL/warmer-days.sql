create database companyDB;
use companyDB;
create table weather (
    id int primary key,
    recordDate date,
    temperature int
);
insert into weather (id, recordDate, temperature)
VALUES
(1, '2023-06-01', 18),
(2, '2023-06-02', 22),
(3, '2023-06-03', 20),
(4, '2023-06-04', 28);
-- answer here
SELECT w1.id 
from weather w1
JOIN weather w2
on datediff(w1.recordDate, w2.recordDate) = 1
where w1.temperature > w2.temperature;