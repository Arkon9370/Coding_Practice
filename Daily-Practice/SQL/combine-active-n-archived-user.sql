create database companyDB;
use companyDB;
create table ActiveUsers (
    user_id int primary key
);
create table ArchivedUsers (
    user_id int primary key
);
insert into ActiveUsers (user_id)
VALUES
(1),(2),(3);
insert into ArchivedUsers (user_id)
VALUES
(3),(4),(5);
-- answer here
SELECT * 
from ActiveUsers
UNION
SELECT *
from ArchivedUsers;