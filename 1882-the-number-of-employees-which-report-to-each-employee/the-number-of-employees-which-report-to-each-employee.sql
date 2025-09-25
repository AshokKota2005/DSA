select a.employee_id,a.name,count(b.reports_to) reports_count,round(sum(b.age)/count(b.reports_to)) average_age
from employees a join employees b
on a.employee_id = b.reports_to
group by a.employee_id
order by a.employee_id;  