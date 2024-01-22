-- 코드를 입력하세요
SELECT USED_GOODS_USER.USER_ID,USED_GOODS_USER.NICKNAME,
    concat(USED_GOODS_USER.city," ",USED_GOODS_USER.street_address1," ",USED_GOODS_USER.street_address2) as 전체주소,
    concat(substring(USED_GOODS_USER.tlno,1,3) ,"-",substring(USED_GOODS_USER.tlno,4,4), "-", substring(USED_GOODS_USER.tlno,8,4))  as 전화번호

from USED_GOODS_BOARD join USED_GOODS_USER on USED_GOODS_USER.user_id = USED_GOODS_BOARD.writer_id

group by USED_GOODS_USER.user_id

having count(USED_GOODS_BOARD.writer_id) >= 3

order by USED_GOODS_USER.user_id desc