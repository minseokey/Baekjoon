-- 코드를 작성해주세요
select c.id
from ecoli_data as g join ecoli_data as p on g.id = p.parent_id and g.parent_id is null join ecoli_data as c on p.id = c.parent_id
where c.id is not null
order by c.id