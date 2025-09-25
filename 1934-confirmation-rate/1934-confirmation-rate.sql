select b.usr user_id,ifnull(round(a.cnt/b.ch,2),0)  confirmation_rate
from (select user_id,count(action) cnt
from confirmations
where action = 'confirmed'
group by user_id) a right join (select s.user_id usr,count(action) ch
from signups s left join confirmations c
on s.user_id = c.user_id 
group by s.user_id) b
on a.user_id = b.usr; 