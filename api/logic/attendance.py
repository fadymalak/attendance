from venv import create
from api.models import STATUS, Employee , LogType
from api.service.attendance import AttendanceService , LogService
from api.service.employee import EmployeeService
from rest_framework.exceptions import APIException
from rest_framework import status
class BadRequest(APIException):
    status_code = 400
    default_detail = 'Bad Request'
    default_code = 'bad_request'


def _check_user_attendance_exists(user):
    employee= EmployeeService.get_employee_by_id(user)
    attendance = AttendanceService.get_create_attendacne_by_user(employee)
    return attendance

def create_attend_login(user,data:dict):
    attendance,created = _check_user_attendance_exists(user)
    if attendance.status == STATUS.PENDING and not created :
        raise BadRequest
    elif attendance.status == STATUS.COMPLETED and not created:
        attendance.status = STATUS.PENDING
        attendance.save()
    log = LogService.create_log(attendance,data)
    attendance = AttendanceService.get_attendacne_by_id(id=attendance.id)
    return attendance

def create_attend_logout(user,data):
    attendance,created = _check_user_attendance_exists(user)
    if attendance.status == STATUS.PENDING:
        attendance.status = STATUS.COMPLETED
        log = LogService.create_log(attendance,data)
        attendance.save()
        attendance = AttendanceService.get_attendacne_by_id(id=attendance.id)
        return attendance
    raise BadRequest

def list_attend(user_id:int):
    employee = EmployeeService.get_employee_by_id(user_id)
    attend_list = AttendanceService.list_attendance(employee.id)
    return attend_list

