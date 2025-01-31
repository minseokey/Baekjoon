-- 코드를 입력하세요
select flavor
from first_half join (select flavor, sum(total_order) as new_total
                      from july
                      group by FLAVOR) as t using(flavor)
order by new_total + total_order desc
limit 3
    