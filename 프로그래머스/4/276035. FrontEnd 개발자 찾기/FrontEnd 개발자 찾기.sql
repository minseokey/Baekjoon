-- 코드를 작성해주세요
select distinct ID, EMAIL, FIRST_NAME, LAST_NAME
from skillcodes s join developers d on (s.category = "Front End" and s.code & d.skill_code = s.code)
order by id