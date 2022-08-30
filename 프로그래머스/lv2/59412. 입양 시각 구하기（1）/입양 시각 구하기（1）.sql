-- 코드를 입력하세요
SELECT hour(datetime) as "HOUR", count(*)
from Animal_outs
where hour(datetime) between 9 and 19
group by hour(datetime)
order by HOUR