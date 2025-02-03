-- 코드를 입력하세요
SELECT u.USER_ID, u.NICKNAME, sum(price) as TOTAL_SALES
from USED_GOODS_BOARD b join USED_GOODS_USER u on b.status = "DONE" and b.writer_id = u.user_id
group by u.user_id
having sum(price) >= 700000 
order by total_sales