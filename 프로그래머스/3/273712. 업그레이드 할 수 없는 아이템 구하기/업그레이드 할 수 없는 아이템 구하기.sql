-- 코드를 작성해주세요

select ITEM_ID,ITEM_NAME,RARITY
from (select p.item_id
        from item_tree p left join item_tree c on c.parent_item_id = p.item_id
        where c.item_id is null) t join item_info using(item_id)

order by item_id desc
        