-- 코드를 작성해주세요
select EMP_NO, EMP_NAME, case when avg(score) >= 96 then "S"
                             when avg(score) >= 90 then "A"
                             when avg(score) >= 80 then "B"
                            else "C" end as GRADE, 
                        case when avg(score) >= 96 then sal * 0.2
                             when avg(score) >= 90 then sal * 0.15
                             when avg(score) >= 80 then sal * 0.1
                            else 0 end as BONUS
from HR_DEPARTMENT d join HR_EMPLOYEES e using(dept_id) join HR_GRADE g using(emp_no)
group by emp_no, emp_name