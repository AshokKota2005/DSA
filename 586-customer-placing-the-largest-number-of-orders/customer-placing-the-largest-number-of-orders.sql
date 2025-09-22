select customer_number
from orders
group by customer_number
having count(customer_number) = (
    select max(customer_count) from (select count(customer_number) as customer_count
from orders
group by customer_number) as t );