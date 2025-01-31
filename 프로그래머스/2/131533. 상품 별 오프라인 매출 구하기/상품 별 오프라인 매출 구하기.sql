-- 코드를 입력하세요
SELECT PRODUCT_CODE, (price * sum(sales_amount)) SALES
from product join offline_sale using(product_id)
group by product_id
order by sales desc, PRODUCT_CODE
