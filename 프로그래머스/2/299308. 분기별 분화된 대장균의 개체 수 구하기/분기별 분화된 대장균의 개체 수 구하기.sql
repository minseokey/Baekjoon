-- 코드를 작성해주세요
select concat(ceil(month(DIFFERENTIATION_DATE) / 3), "Q") as QUARTER, count(*) as ECOLI_COUNT
from ECOLI_DATA
group by quarter
order by quarter