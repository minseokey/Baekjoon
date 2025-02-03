-- 코드를 입력하세요
SELECT  concat("/home/grep/src/",Board_id, "/",file_id,file_name,file_ext) as file_path
from USED_GOODS_BOARD join USED_GOODS_FILE using(Board_id)
where views = (select max(views)
               from USED_GOODS_BOARD)

order by file_id desc
