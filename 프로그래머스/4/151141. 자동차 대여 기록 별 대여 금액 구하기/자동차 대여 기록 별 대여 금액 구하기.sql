-- 코드를 입력하세요
SELECT HISTORY_ID, case when datediff(end_date, start_date) + 1 >= 90 then round(daily_fee * (datediff(end_date, start_date) + 1) * (100 - (select DISCOUNT_RATE
                                                                                                                                    from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                                                                                                                                    where car_type = "트럭" and DURATION_TYPE = "90일 이상")) / 100)
                        when datediff(end_date, start_date) + 1 >= 30 then round(daily_fee * (datediff(end_date, start_date) + 1) * (100 - (select DISCOUNT_RATE
                                                                                                                                    from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                                                                                                                                    where car_type = "트럭" and DURATION_TYPE = "30일 이상")) / 100)
                        when datediff(end_date, start_date) + 1 >= 7 then round(daily_fee * (datediff(end_date, start_date) + 1) * (100 - (select DISCOUNT_RATE
                                                                                                                                    from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                                                                                                                                    where car_type = "트럭" and DURATION_TYPE = "7일 이상")) / 100)
                        else daily_fee * (datediff(end_date, start_date) + 1) end as FEE
from CAR_RENTAL_COMPANY_CAR C join CAR_RENTAL_COMPANY_RENTAL_HISTORY H using(car_id)
where car_type = "트럭"
order by fee desc, history_id desc

