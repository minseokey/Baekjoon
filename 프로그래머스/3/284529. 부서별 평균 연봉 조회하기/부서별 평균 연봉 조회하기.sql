-- 코드를 작성해주세요
select dept_id, dept_name_en, round(avg(sal),0) as avg_sal
from hr_department join hr_employees using(dept_id)
group by dept_id
order by avg(sal) desc