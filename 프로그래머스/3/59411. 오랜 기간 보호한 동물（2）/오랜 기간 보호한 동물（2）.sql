-- 코드를 입력하세요
SELECT i.ANIMAL_ID, i.NAME
from animal_outs o join animal_ins i using(ANIMAL_ID)
order by datediff(o.datetime, i.datetime) + 1 desc
limit 2