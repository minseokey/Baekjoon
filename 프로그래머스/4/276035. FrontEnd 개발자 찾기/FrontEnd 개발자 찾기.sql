-- 코드를 작성해주세요
select distinct(ID),EMAIL,FIRST_NAME,LAST_NAME
from skillcodes join developers
where skill_code & code = code and category = "Front End"
order by id