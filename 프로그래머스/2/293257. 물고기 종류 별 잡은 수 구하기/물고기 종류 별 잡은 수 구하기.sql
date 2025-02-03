-- 코드를 작성해주세요
select count(*) as FISH_COUNT, FISH_NAME
from FISH_INFO join FISH_NAME_INFO using(FISH_TYPE)
group by fish_name
order by fish_count desc