-- 코드를 입력하세요
SELECT car_id
from CAR_RENTAL_COMPANY_CAR join CAR_RENTAL_COMPANY_RENTAL_HISTORY using (car_id) 
where car_type = "세단" and month(start_date) = "10"
group by car_id
order by car_id desc