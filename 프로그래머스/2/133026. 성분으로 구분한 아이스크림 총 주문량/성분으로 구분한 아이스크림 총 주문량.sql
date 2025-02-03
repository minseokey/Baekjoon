-- 코드를 입력하세요
SELECT INGREDIENT_TYPE, sum(total_order) as TOTAL_ORDER
from first_half join icecream_info using(flavor)
group by ingredient_type
