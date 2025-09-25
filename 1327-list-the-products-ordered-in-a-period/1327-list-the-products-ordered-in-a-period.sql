select b.product_name product_name,a.units as unit
from (select product_id,sum(unit) as units
from orders 
where monthname(order_date) = 'February' and year(order_date) = '2020'
group by product_id) a join products b
on a.product_id = b.product_id and a.units >= 100
;