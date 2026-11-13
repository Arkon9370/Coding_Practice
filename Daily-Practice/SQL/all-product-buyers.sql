-- assuming the DB, table and values are present ->
select customer_id
from Customer 
group by customer_id
having count(distinct product_key) = (select count(*) from Product )
order by customer_id asc;