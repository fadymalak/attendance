from api.models import Attendance , AttendanceLog , CURRENT_USER_MODEL
import datetime
from typing import Union
from django.core.exceptions import ObjectDoesNotExist
class AttendanceService():
    def create_attendance(user:CURRENT_USER_MODEL,data:dict) -> Attendance:
        attendance = Attendance.objects.prefetch_related('logs').create(user=user,**data)
        return attendance

    def get_attendacne_by_id(id:int)-> Attendance:
        try:
            attendance = Attendance.objects.prefetch_related('logs').get(id=id)
        except ObjectDoesNotExist:
            return None 

        return attendance

    def list_attendance(employee_id):
        attendances = Attendance.objects.filter(employee=employee_id).all()
        return attendances

    def get_create_attendacne_by_user(employee:CURRENT_USER_MODEL,data:Union[dict,None]=None)-> Attendance:
        attendance = Attendance.objects\
                        .filter(
                            employee=employee,
                            date=datetime.date.today()
                            )\
                            .get_or_create(employee=employee,\
                                date=datetime.date.today(),
                                )
        return attendance
    
    def list_attendace_by_user(employee_id):
        ''' List monthly user attendance'''
        attendances = Attendance.objects.filter(
                                employee__id=employee_id,\
                                    date__month=datetime.date.today().month\
                                        )\
                                        .select_related("logs")\
                                            .all()
        return attendances


class LogService():
    def create_log(attendance:Attendance,data:dict)-> AttendanceLog:
        log = AttendanceLog.objects.create(attendance=attendance,**data)
        return log

    def get_latest(attendance_id:int)-> AttendanceLog:
        log = AttendanceLog.objects\
                    .filter(attendance__id=attendance_id)\
                        .order_by("-created_at")\
                            .first()
        return log
    

