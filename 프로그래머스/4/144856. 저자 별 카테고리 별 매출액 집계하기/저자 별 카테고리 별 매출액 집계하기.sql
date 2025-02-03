-- 코드를 입력하세요
SELECT AUTHOR_ID,AUTHOR_NAME,CATEGORY, sum(sales * price) as TOTAL_SALES
from book b join author a using(author_id) join book_sales s using(book_id)
where date_format(sales_Date, "%Y-%m") = "2022-01"
group by author_id, category 
order by author_id, category desc