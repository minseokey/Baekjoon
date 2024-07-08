with total_count as (
    select count(*) as cnt
    from ecoli_data
)

select ID, 
       case 
           when size_of_colony <= (select max(size_of_colony)
                                   from ecoli_data
                                   order by size_of_colony
                                   limit 1 offset (select cnt / 4 - 1 from total_count)
                                  ) then 'LOW'
           when size_of_colony <= (select max(size_of_colony)
                                   from ecoli_data
                                   order by size_of_colony
                                   limit 1 offset (select cnt / 2 - 1 from total_count)
                                  ) then 'MEDIUM'
           when size_of_colony <= (select max(size_of_colony)
                                   from ecoli_data
                                   order by size_of_colony
                                   limit 1 offset (select cnt / 4 * 3 - 1 from total_count)
                                  ) then 'HIGH'
           else 'CRITICAL'
       end as colony_name
from ecoli_data
order by id;
