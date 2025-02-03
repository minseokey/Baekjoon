-- 코드를 입력하세요
select CATEGORY, price as MAX_PRICE, PRODUCT_NAME
from food_product p
where price = (select max(price)
               from food_product
               group by category
               having category = p.category) and category in ('과자', '국', '김치', '식용유')
order by max_price desc