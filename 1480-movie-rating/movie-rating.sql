select a.name results
from (select u.name name,count(distinct movie_id) sr
from movierating m right join users u
on m.user_id = u.user_id
group by m.user_id
order by sr desc,name
limit 1) a 
union all
select b.t results
from (select m.movie_id,title t,sum(rating)/count(rating) cnt
from movierating mr right join movies m
on m.movie_id = mr.movie_id 
where month(created_at) = 2 and year(created_at) = 2020
group by m.movie_id
order by cnt desc,title
limit 1) b;
;