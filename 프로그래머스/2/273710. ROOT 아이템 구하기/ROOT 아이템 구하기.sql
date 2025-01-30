-- 코드를 작성해주세요
select item_id, item_name
from item_tree join item_info using(item_id)
where parent_item_id is null
order by item_id