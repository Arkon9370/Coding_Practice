create database companyDB;
use companyDB;
create table World (
    name VARCHAR(50) PRIMARY KEY,
    continent varchar(50),
    area int,
    population int,
    gdp bigint
);
insert into World (name, continent, area, population, gdp)
VALUES
('Greenland','North America',652230,25500100,20343000000),
('Iceland','Europe',28748,2831741,12960000000),
('Brazil','South America',2381741,37100000,188681000000),
('Fiji','Oceania',468,78115,3712000000),
('Nepal','Asia',1246700,20609294,100990000000);
-- your answer here
SELECT name, population, area 
from World
where (population >= 25000000 or area >= 3000000);