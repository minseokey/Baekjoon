-- 코드를 작성해주세요
select count(*) as count
from ecoli_data
where GENOTYPE & 2 != 2 and (GENOTYPE & 1 = 1 or GENOTYPE & 4 = 4)
