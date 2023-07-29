-- 코드를 입력하세요
SELECT date_format(SALES_DATE,"%Y-%m-%d") as SALES_DATE,PRODUCT_ID,IFNULL(USER_ID,null),SALES_AMOUNT
from (select SALES_DATE,PRODUCT_ID,USER_ID,SALES_AMOUNT 
      from online_sale
      union
      select SALES_DATE,PRODUCT_ID, null as user_id, SALES_AMOUNT 
      from offline_sale
      ) as sale
where year(sales_date) = "2022" and month(sales_date) = "03"
order by sales_date , product_id, user_id