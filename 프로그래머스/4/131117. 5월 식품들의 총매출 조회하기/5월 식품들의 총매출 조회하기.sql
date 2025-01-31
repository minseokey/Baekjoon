-- 코드를 입력하세요
SELECT PRODUCT_ID, PRODUCT_NAME, sum(amount) * price  as TOTAL_SALES
from FOOD_PRODUCT join FOOD_ORDER using(PRODUCT_ID)
where date_format(PRODUCE_DATE, "%Y-%m") = "2022-05"
group by product_id
order by total_sales desc, product_id