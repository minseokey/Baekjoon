select ID, CASE
        when ntile(4) over(order by SIZE_OF_COLONY DESC) = 1 then 'CRITICAL'
        when ntile(4) over(order by SIZE_OF_COLONY DESC) = 2 then 'HIGH'
        when ntile(4) over(order by SIZE_OF_COLONY DESC) = 3 then 'MEDIUM'
        when ntile(4) over(order by SIZE_OF_COLONY DESC) = 4 then 'LOW'
    END as COLONY_NAME
from ecoli_data
order by id