select a.class 
from (select class,count(class) cnt
from courses
group by class) a
where a.cnt >= 5;