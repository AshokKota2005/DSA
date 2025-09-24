select u.user_id as buyer_id,u.join_date as join_date,ifnull(a.coi,0) as orders_in_2019
from users u left join (select buyer_id,count(order_id) coi
from orders
where order_date >= '2019-01-01' and order_date <= '2019-12-31'
group by buyer_id) a
on u.user_id = a.buyer_id;