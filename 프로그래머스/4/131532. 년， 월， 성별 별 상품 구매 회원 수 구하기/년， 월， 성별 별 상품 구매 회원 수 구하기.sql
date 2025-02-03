-- 코드를 입력하세요
SELECT year(sales_date) as YEAR, month(sales_date) as MONTH, GENDER, count(user_id) as USERS
from user_info join (select *
                     from online_sale
                     group by year(sales_date), month(sales_date), user_id) t using(USER_ID)
where gender is not null
group by year(sales_date), month(sales_date), gender
order by year(sales_date), month(sales_date), gender