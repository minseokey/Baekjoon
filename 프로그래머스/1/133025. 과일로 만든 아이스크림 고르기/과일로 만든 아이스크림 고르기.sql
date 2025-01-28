-- 코드를 입력하세요
SELECT FLAVOR
from FIRST_HALF join ICECREAM_INFO using(FLAVOR)
where total_order > 3000 and INGREDIENT_TYPE = "fruit_based"
order by total_order desc