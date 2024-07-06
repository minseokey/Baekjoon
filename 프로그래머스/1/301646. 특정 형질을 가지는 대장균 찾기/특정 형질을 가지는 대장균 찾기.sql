-- 코드를 작성해주세요
select count(*) as count
from ecoli_data
where bin(genotype) & 5 > 0 and bin(genotype) & 7 = bin(genotype) & 5