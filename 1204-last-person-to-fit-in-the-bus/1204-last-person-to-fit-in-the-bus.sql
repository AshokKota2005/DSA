select person_name
from (select *,sum(weight) over(order by turn rows between unbounded preceding and current row) t
from queue) a
where a.t <= 1000
order by a.t desc
limit 1;