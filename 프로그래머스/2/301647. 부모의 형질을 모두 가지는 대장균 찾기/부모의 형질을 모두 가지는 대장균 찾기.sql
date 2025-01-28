-- 코드를 작성해주세요
select c.id as id, c.genotype as genotype, p.genotype as PARENT_GENOTYPE
from ecoli_data as p join ecoli_data as c on p.id = c.parent_id
where p.genotype & c.genotype = p.genotype

