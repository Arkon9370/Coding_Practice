-- assuming DB, TABLES and VALUES are present
select e1.name 
from Employees as e1
join Employees as e2
on e1.manager_id = e2.employee_id
where e1.salary > e2.salary;