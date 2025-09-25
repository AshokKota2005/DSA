select user_id,concat(upper(substr(lower(name),1,1)),substr(lower(name),2,length(name)-1 )) as name
from Users
order by user_id;  