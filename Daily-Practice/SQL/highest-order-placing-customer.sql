-- assuming DB, TABLE and VALUES are present
select customer_number 
from Orders
group by customer_number
order by count(order_number) desc
limit 1;