-- 코드를 작성해주세요
select sum(SCORE) as score ,EMP_NO,EMP_NAME,POSITION,EMAIL

from hr_employees join hr_grade using(emp_no)
where year = 2022
group by emp_no
order by sum(score) desc
limit 1
