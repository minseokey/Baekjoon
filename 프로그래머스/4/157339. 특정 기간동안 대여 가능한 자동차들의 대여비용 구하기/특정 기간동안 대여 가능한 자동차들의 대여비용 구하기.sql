-- 코드를 입력하세요
SELECT CAR_ID,CAR_TYPE, (select round(30 * sum(DAILY_FEE) * (100 - discount_rate) / 100)
                        from CAR_RENTAL_COMPANY_CAR join CAR_RENTAL_COMPANY_DISCOUNT_PLAN using(car_type)
                        where car.CAR_ID = CAR_ID and duration_type = "30일 이상"
                        group by car_id) as FEE 
                     
from CAR_RENTAL_COMPANY_CAR car join CAR_RENTAL_COMPANY_RENTAL_HISTORY rental using(car_id)

where car_id in (select CAR_ID
                from CAR_RENTAL_COMPANY_RENTAL_HISTORY
                group by CAR_ID
                having min(start_date) > date('2022-11-30') or max(end_date) < date('2022-11-01'))
                and car_type in ("세단","SUV")
                and (select 30 * sum(DAILY_FEE) * (100 - discount_rate) / 100
                     from CAR_RENTAL_COMPANY_CAR join CAR_RENTAL_COMPANY_DISCOUNT_PLAN using(car_type)
                     where car.CAR_ID = CAR_ID and duration_type = "30일 이상"
                     group by car_id) between 500000 and 2000000

group by car_id
order by FEE desc, car_type, car_id desc

                
                

