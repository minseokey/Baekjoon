-- 코드를 입력하세요
SELECT PRODUCT_ID,PRODUCT_NAME,price * sum(amount) as total_sales
From Food_product join (select *
                        from food_order
                        where produce_date between "2022-05-01" and "2022-05-31") as o using(product_id)
group by product_id
order by total_sales desc, product_id