-- 코드를 작성해주세요
select count(*) as fish_count, fish_name
from fish_name_info join fish_info using(fish_type)
group by fish_name
order by fish_count desc