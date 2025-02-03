-- 코드를 입력하세요

SELECT year(s.sales_date) as YEAR, month(s.sales_date) as MONTH, count(*) as PURCHASED_USERS,
     round(count(*)/(select count(*)
                     from user_info
                     where year(joined) = 2021), 1) as PUCHASED_RATIO

from user_info u left join (select sales_date, user_id
                            from online_sale
                            group by year(sales_Date), month(sales_date), user_id) s using(user_id)

where year(u.joined) = 2021 and s.sales_date is not null

group by year(s.sales_Date), month(s.sales_date)
order by year(s.sales_Date), month(s.sales_date)
