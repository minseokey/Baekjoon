-- 코드를 입력하세요
select distinct base.car_id, case when temp.car_id is null then "대여 가능"
                                else "대여중" end as AVAILABILITY
from  CAR_RENTAL_COMPANY_RENTAL_HISTORY base left join (SELECT distinct CAR_ID
                                                        from CAR_RENTAL_COMPANY_RENTAL_HISTORY
                                                        where "2022-10-16" between start_date and end_date) temp  on base.car_id = temp.car_id

order by base.car_id desc