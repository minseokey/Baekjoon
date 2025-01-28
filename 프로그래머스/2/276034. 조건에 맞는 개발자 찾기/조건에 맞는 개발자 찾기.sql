-- 코드를 작성해주세요
select distinct ID,EMAIL,FIRST_NAME,LAST_NAME
from developers as d join skillcodes as s on (d.SKILL_CODE & s.code) = s.code and s.Name in ("C#","Python")
order by id