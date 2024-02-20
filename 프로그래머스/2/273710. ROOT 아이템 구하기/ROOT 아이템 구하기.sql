-- 코드를 작성해주세요
select item_id, item_name
from item_info join item_tree using(item_id)
where parent_item_id is null
order by item_id
