-- 코드를 작성해주세요
select DEPT_ID	,DEPT_NAME_EN, round(avg(SAL)) as AVG_SAL
from HR_DEPARTMENT join HR_EMPLOYEES using(DEPT_ID)
group by dept_id
order by avg_sal desc