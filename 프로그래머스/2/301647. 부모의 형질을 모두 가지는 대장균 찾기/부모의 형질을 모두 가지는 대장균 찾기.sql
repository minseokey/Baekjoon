-- 코드를 작성해주세요
select son.id as ID, son.genotype as GENOTYPE , parent.genotype as PARENT_GENOTYPE
from ecoli_data parent join ecoli_data son on parent.id = son.parent_id
where parent.genotype & ~son.genotype = 0
order by ID
