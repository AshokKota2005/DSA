select distinct id,case 
when idd is NULL then 'Root'
when iddd > 0 then 'Inner'
else 'Leaf'
end as 'type'
from 
(select distinct a.id id,a.p_id idd,b.id iddd
from tree a left join tree b
on a.id = b.p_id) k;