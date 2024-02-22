select distinct(id) ,EMAIL,FIRST_NAME,LAST_NAME
from skillcodes join developers
where skill_code & CODE = CODE and name in ("Python","C#")
order by id