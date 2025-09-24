
select a.student_id,a.student_name,a.subject_name,ifnull(b.cnt,0) attended_exams
from (select * from students s,subjects b) a 
    left join 
    (select student_id,subject_name,count(subject_name) cnt from examinations group by student_id,subject_name) b 
    on a.student_id = b.student_id and a.subject_name = b.subject_name
    order by student_id,subject_name;
