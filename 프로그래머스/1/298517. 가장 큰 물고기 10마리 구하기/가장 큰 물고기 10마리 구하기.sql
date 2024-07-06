-- 코드를 작성해주세요

select ID, length
from (select id, ifnull(length, 10) as length
     from fish_info
     order by length desc
     limit 10) a
order by length desc, id
limit 10