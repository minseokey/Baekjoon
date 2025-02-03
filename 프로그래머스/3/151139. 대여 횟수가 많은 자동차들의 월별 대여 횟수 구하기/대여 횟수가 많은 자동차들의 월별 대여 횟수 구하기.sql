-- 코드를 입력하세요
SELECT month(start_date) as MONTH, CAR_ID, count(*) RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY h
where date_format(start_date, '%Y-%m') between '2022-08' and '2022-10' and (select count(*)
                                                                            from CAR_RENTAL_COMPANY_RENTAL_HISTORY
                                                                            where date_format(start_date, '%Y-%m') between '2022-08' and '2022-10' and h.car_id = car_id) >= 5 
group by car_id, month(start_Date)
having count(*) > 0
order by month, car_id desc