select visited_on,b.summ amount,b.avgg average_amount
from (select visited_on,sum(amountt) over(order by visited_on rows between 6 preceding and CURRENT ROW) summ,ROW_NUMBER() OVER (ORDER BY visited_on) rankk,round(sum(amountt) over(order by visited_on rows between 6 preceding and CURRENT ROW)/7,2)  avgg
from (select *,sum(amount) amountt
from customer
group by visited_on) a) b
where b.rankk > 6
;