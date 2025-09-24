select round((d.y/c.x)*100,2) immediate_percentage
from (select count(*) x from (select *,row_number() over(partition by customer_id order by order_date asc) t from delivery) a where a.t = 1) c,
     (select count(*) y from (select *,row_number() over(partition by customer_id order by order_date asc) s from delivery) b where b.s = 1 and order_date = customer_pref_delivery_date) d;
