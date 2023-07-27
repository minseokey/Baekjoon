-- 코드를 입력하세요
SELECT WAREHOUSE_ID,WAREHOUSE_NAME,ADDRESS,IFNULL(FREEZER_YN,"N")

from food_warehouse
where warehouse_name like "%경기%"
