-- 코드를 작성해주세요
select item_id, item_name, rarity
from item_info join item_tree using(item_id)
where parent_item_id in (select ITEM_ID
                        from item_info  
                        where rarity = "RARE" and item_id in (select parent_item_id
                                                              from item_tree
                                                              where parent_item_id is not null))

order by item_id desc