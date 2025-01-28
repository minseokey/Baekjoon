-- 코드를 입력하세요

select date_format(SALES_DATE,"%Y-%m-%d"),PRODUCT_ID,USER_ID,SALES_AMOUNT

from ((SELECT USER_ID,PRODUCT_ID,SALES_AMOUNT,SALES_DATE
        from online_sale)

        union all

       (select null as USER_ID, PRODUCT_ID,SALES_AMOUNT,SALES_DATE
        from offline_sale)) as t
        
where year(sales_date) = 2022 and month(sales_date) = 3
order by sales_date, product_id, user_id