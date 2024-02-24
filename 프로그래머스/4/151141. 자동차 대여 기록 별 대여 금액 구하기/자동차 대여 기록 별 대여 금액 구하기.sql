-- 코드를 입력하세요
select history_id, 
    case
        when isnull(plan_id) then convert((datediff(end_date, start_date) + 1)*daily_fee ,signed)
        else convert(((datediff(end_date, start_date)+1) * daily_fee / 100) * (100 - discount_rate) ,signed)
    end as "FEE"
from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
        right join
    (SELECT car_type, history_id, end_date, start_date, daily_fee,
        case 
            when datediff(end_date, start_date) >= 90  then "90일 이상"
            when datediff(end_date, start_date) between 30 and 89 then "30일 이상"
            when datediff(end_date, start_date) between 7 and 29 then "7일 이상"
        end as "DURATION_TYPE"
    from CAR_RENTAL_COMPANY_CAR join CAR_RENTAL_COMPANY_RENTAL_HISTORY using(car_id)
    where car_type = "트럭"
    ) as duration
    
    using(car_type, duration_type)
order by FEE desc ,history_id desc