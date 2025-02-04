-- 코드를 입력하세요
SELECT USER_ID, NICKNAME, concat(city, " ",STREET_ADDRESS1, " ", STREET_ADDRESS2) 전체주소, concat(substr(tlno,1,3),"-",substr(tlno,4,4),"-",substr(tlno,8,4)) as 전화번호
from USED_GOODS_BOARD B join USED_GOODS_USER U on B.writer_id = U.user_id
group by B.Writer_id
having count(B.writer_id) >= 3
order by user_id desc