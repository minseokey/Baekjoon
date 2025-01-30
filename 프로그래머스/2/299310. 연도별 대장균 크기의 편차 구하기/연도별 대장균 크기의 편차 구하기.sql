-- 코드를 작성해주세요
select YEAR(DIFFERENTIATION_DATE) as YEAR,
        (select max(size_of_colony)
        from ecoli_data
        where YEAR(e.DIFFERENTIATION_DATE) = YEAR(DIFFERENTIATION_DATE)
        group by year(DIFFERENTIATION_DATE)) - size_of_colony as YEAR_DEV, ID
from ecoli_data e
order by year, year_dev
