-- 코드를 입력하세요
SELECT concat("/home/grep/src/" , board_id, "/" , file_id , file_name ,  File_ext) as FILE_PATH
from USED_GOODS_BOARD join USED_GOODS_FILE using(Board_Id)
where Board_id = (select Board_Id
                    from used_goods_board
                    order by views desc limit 1)
order by file_id desc

# select *
# from USED_GOODS_BOARD

