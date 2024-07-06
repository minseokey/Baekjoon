-- 코드를 작성해주세요
select ID, fish_name, length
from fish_name_info join fish_info using (fish_type)
where (length, fish_type) in (select max(length), fish_type
                               from fish_info
                               group by fish_type)
                               
order by id
