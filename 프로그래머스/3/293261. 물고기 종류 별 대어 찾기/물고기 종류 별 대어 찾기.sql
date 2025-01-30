-- 코드를 작성해주세요
select fi.id, fni.fish_name, fi.length  
from fish_info fi join fish_name_info fni using(fish_type)
where fi.id = (select id
               from fish_info
               where fi.fish_type = fish_type
               order by length desc
               limit 1)
order by fi.id