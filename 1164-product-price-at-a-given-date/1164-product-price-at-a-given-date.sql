select c.product_id product_id,ifnull(d.new_price,10) price from (select * from (select *,row_number() over(partition by product_id order by change_date desc) rankkk from products) a where a.rankkk = 1) c left join 
              (select * from (select *,row_number() over(partition by product_id order by change_date desc) rankk from products where change_date <= '2019-08-16') b where b.rankk = 1) d
              on c.product_id = d.product_id; 
; 