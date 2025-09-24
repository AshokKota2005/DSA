(select p.product_id,p.product_name
from product p join sales s
on p.product_id = s.product_id
where s.sale_date between '2019-01-01' and '2019-03-31')
except
(select p.product_id,p.product_name
from product p join sales s
on p.product_id = s.product_id
where s.sale_date not between '2019-01-01' and '2019-03-31');