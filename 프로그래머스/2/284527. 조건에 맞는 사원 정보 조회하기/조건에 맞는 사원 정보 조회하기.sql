-- 코드를 작성해주세요
select sum(score) as SCORE, EMP_NO, EMP_NAME, POSITION, EMAIL
from HR_DEPARTMENT d join HR_EMPLOYEES e using(DEPT_ID) join HR_GRADE g using(EMP_NO)
group by emp_no
order by score desc
limit 1