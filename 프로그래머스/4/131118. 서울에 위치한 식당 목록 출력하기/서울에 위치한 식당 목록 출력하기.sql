-- 코드를 입력하세요
SELECT REST_ID,REST_NAME,FOOD_TYPE,FAVORITES,ADDRESS, round(avg(REVIEW_SCORE),2)	as SCORE
from rest_info join rest_review using(rest_id)
where Address like "서울%"
group by rest_id
order by SCORE desc, favorites desc