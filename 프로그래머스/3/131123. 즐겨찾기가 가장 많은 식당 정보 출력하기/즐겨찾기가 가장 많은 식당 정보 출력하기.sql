-- 코드를 입력하세요
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
from rest_info i
where favorites = (select max(favorites)
                   from rest_info
                   where i.food_type = food_type
                   group by food_type) 
order by food_type desc