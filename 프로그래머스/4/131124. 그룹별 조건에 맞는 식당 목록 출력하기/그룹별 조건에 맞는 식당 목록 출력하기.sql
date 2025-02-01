-- 코드를 입력하세요
SELECT MEMBER_NAME, REVIEW_TEXT, date_format(review_date, "%Y-%m-%d")as REVIEW_DATE
from MEMBER_PROFILE join REST_REVIEW using(MEMBER_ID)
where member_id = (select member_id
                   from rest_review
                   group by member_id
                   order by count(*) desc 
                   limit 1)
                   
order by review_date, REVIEW_TEXT