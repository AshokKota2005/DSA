select user_id,time_stamp as last_stamp
from (select *,dense_rank() over(partition by user_id order by time_stamp desc) as sp
from logins
where year(time_stamp) = 2020) a
where a.sp = 1;