-- 코드를 입력하세요
SELECT AUTHOR_ID,AUTHOR_NAME,CATEGORY,sum(price * sales) as TOTAL_SALES
from book_sales join(select * 
                    from book inner join author using (author_id) ) as t 
                    using(book_id)

where sales_date like "%2022-01%"
group by author_name, category
order by author_id, category desc