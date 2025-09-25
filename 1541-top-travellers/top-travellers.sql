select name,ifnull(b.sd,0) as travelled_distance
from users a left join (
select user_id,sum(distance) as sd
from rides
group by user_id) b
on a.id = b.user_id
order by sd desc,a.name;
