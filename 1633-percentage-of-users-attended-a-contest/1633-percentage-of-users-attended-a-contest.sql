select b.contest_id contest_id,round((count(b.user_id)/a.cu)*100,2) as percentage
from (select count(user_id) cu
      from Users) a      ,Register b
group by b.contest_id
order by percentage desc,b.contest_id;

