-- 코드를 작성해주세요
select p.id, count(c.ID) as child_count
from ecoli_data as p left join ecoli_data as c on p.id = c.parent_id 
group by p.id
order by p.id
