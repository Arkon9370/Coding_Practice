create database companyDB;
use companyDB;
create table employees(
    employee_id int PRIMARY KEY,
    name VARCHAR(50)
);
create table salaries(
    employee_id int PRIMARY KEY,
    salary int
);
insert into employees (employee_id, name)
VALUES 
(1, Aarav), 
(2, Neha), 
(3, Rohan);
insert into salaries (employee_id, salary)
VALUES
(1, 50000),
(3, 60000);
-- answer here
select e.employee_id, e.name, s.salary
from employees e
inner join salaries s
on e.employee_id = s.employee_id;