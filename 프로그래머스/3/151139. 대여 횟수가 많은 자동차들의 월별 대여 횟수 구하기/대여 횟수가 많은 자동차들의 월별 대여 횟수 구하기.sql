-- 코드를 입력하세요
SELECT MONTH(start_date) as month, CAR_ID, count(*) as RECORDS
from (select car_id
      from CAR_RENTAL_COMPANY_RENTAL_HISTORY
      where start_date between "2022-08-01" and "2022-10-31"
      group by car_id
      having count(*) >= 5) as C 
      join
      car_rental_company_rental_history using(car_id)

where start_date between "2022-08-01" and "2022-10-31"
group by month, car_id
having count(*) > 0
order by month, car_id desc