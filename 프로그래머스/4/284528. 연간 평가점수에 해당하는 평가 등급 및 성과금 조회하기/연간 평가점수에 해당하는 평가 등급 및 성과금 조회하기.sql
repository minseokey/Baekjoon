with hr_grade_with as (
    select emp_no, avg(score) as sc
    from hr_grade
    group by emp_no)

select emp_no, emp_name,
    case when sc >= 96 then "S"
         when sc >= 90 then "A"
         when sc >= 80 then "B"
         else "C"
         end as "GRADE",
    
    case when sc >= 96 then (sal/100)*20
         when sc >= 90 then (sal/100)*15
         when sc >= 80 then (sal/100)*10
         else 0
         end as "BONUS"
from hr_employees join hr_grade_with using(emp_no)


order by emp_no