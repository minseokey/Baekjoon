with ranktable as (
    select id, size_of_colony, ntile(4) over(order by size_of_colony) as quantile
    from ecoli_data
)

select ID, 
       case 
           when quantile = 1 then 'LOW'
           when quantile = 2 then 'MEDIUM'
           when quantile = 3 then 'HIGH'
           else 'CRITICAL'
       end as colony_name
from ranktable
order by id