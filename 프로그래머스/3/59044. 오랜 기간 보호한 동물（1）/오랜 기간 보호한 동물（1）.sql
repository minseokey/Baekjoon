-- 코드를 입력하세요
SELECT I.NAME, I.DATETIME
from animal_ins I left join animal_outs O using(animal_id)
where O.datetime is null
order by I.datetime
limit 3