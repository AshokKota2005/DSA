select employee_id,department_id
from (select *,row_number() over(partition by employee_id order by primary_flag) rankk
from employee) a
where a.rankk = 1;