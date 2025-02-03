-- 코드를 작성해주세요
select ROUTE, concat(round(sum(D_BETWEEN_DIST),1),"km") as TOTAL_DISTANCE, concat(round(sum(D_BETWEEN_DIST)/count(*),2),"km") as AVERAGE_DISTANCE
from SUBWAY_DISTANCE
group by Route
order by sum(D_BETWEEN_DIST) desc