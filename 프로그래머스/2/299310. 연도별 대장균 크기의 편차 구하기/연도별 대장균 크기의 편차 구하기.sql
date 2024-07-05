-- 코드를 작성해주세요
select year(DIFFERENTIATION_DATE) as year,
        (select max(size_of_colony)
        from ecoli_data
        where year(DIFFERENTIATION_DATE) = year) - size_of_colony as year_dev,
        ID
        
from ecoli_data
order by year(DIFFERENTIATION_DATE), year_dev