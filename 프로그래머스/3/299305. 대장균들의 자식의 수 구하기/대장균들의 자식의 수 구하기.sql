-- 코드를 작성해주세요
select a.ID as ID, ifnull(b.count, 0) as CHILD_COUNT
from ecoli_data a left join (select count(*) as count, parent_id
                            from ecoli_data
                            group by parent_id) b on a.id = b.parent_id
order by ID 