-- 코드를 작성해주세요
Select c.Item_ID, c.item_name, c.rarity
from item_Info as p join item_tree as t on p.ITEM_ID = t.PARENT_ITEM_ID join ITEM_INFO as c on c.Item_ID = t.Item_ID
where p.rarity = "RARE"
order by c.item_id desc

