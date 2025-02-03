-- 코드를 입력하세요
SELECT hour(datetime) as HOUR, count(*) as COUNT
from ANIMAL_OUTS
where hour(datetime) between 9 and 20
group by hour(datetime)
order by hour