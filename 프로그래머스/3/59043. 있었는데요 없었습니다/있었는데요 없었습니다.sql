-- 코드를 입력하세요
SELECT ANIMAL_ID, o.NAME
from animal_ins I join animal_outs O using(animal_id)
where I.datetime > O.datetime
order by I.datetime