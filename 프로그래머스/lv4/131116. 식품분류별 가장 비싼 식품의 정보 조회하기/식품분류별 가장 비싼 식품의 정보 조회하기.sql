SELECT category, price,PRODUCT_NAME 
FROM (
  SELECT category, price,PRODUCT_NAME,ROW_NUMBER() OVER (PARTITION BY category ORDER BY price DESC) AS row_num
  FROM FOOD_PRODUCT
  WHERE category IN ('과자', '국', '김치', '식용유')
) AS subquery
WHERE row_num = 1
ORDER BY PRICE DESC;