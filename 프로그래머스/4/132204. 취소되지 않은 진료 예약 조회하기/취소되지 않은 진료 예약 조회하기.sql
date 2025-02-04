-- 코드를 입력하세요
SELECT APNT_NO, PT_NAME, PT_NO, A.MCDP_CD, DR_NAME, APNT_YMD
from PATIENT P join APPOINTMENT A using(PT_NO) join DOCTOR D on D.DR_ID = A.MDDR_ID and D.MCDP_CD = "CS"
where date_format(APNT_YMD,"%Y-%m-%d") = "2022-04-13" and APNT_CNCL_YN = 'N'
order by APNT_YMD