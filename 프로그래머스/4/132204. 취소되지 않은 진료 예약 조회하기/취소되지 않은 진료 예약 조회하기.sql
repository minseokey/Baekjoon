-- 코드를 입력하세요
SELECT appointment.APNT_NO,patient.PT_NAME,patient.PT_NO,doctor.MCDP_CD,doctor.DR_NAME,appointment.APNT_YMD
from patient join appointment on patient.pt_no = appointment.pt_no
             join doctor on appointment.mddr_id = doctor.dr_id

where appointment.apnt_cncl_yn = "N" and date(appointment.apnt_ymd) = "2022-04-13" and appointment.mcdp_cd = "CS"
order by appointment.apnt_ymd