select c.bqn query_name,c.quality quality,IFNULL(c.poor_query_percentage ,0) poor_query_percentage
from
(select b.query_name bqn,round(sum(rating /position)/count(b.query_name),2) quality,round((a.cnt/count(b.query_name)*100),2) poor_query_percentage
from (select query_name,count(rating) cnt
from Queries
where rating < 3
group by query_name) a right join Queries b
on a.query_name = b.query_name
group by b.query_name) c;