-- assuming DB, TABLES and VALUES are present
select * 
from Cinema
where id % 2 != 0 
and description != 'boring'
order by rating desc;