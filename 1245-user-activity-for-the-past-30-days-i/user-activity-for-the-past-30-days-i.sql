select a.activity_date day,a.cnt active_users
from (select activity_date,count(distinct user_id) cnt from activity group by activity_date) a
where a.activity_date >= '2019-06-28' and a.activity_date <= '2019-07-27';