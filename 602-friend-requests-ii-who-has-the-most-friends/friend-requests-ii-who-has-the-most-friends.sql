select requester_id id,y.cnt2  num
from (select requester_id,sum(x.cnt1) as cnt2
from (select requester_id,count(*) cnt1 from requestaccepted group by requester_id
union all
select accepter_id,count(*) from requestaccepted group by accepter_id) x
group by requester_id) y
where y.cnt2 = (select max(z.cnt2)
from (select requester_id,sum(x.cnt1) as cnt2
from (select requester_id,count(*) cnt1 from requestaccepted group by requester_id
union all
select accepter_id,count(*) from requestaccepted group by accepter_id) x
group by requester_id) z);