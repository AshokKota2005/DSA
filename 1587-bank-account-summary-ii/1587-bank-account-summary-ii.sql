select u.name as NAME,a.sp AS BALANCE
from (select account,sum(amount) sp
from transactions
group by account) a join users u
on u.account = a.account
where a.sp > 10000;