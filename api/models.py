from enum import Enum
from django.db import models
from django.contrib.auth.models import User


CURRENT_USER_MODEL = User
# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User,related_name="employee",on_delete=models.CASCADE)


class STATUS(models.TextChoices):
    COMPLETED ="COMPLETED"
    PENDING = "PENDING"


class Attendance(models.Model):
    employee = models.ForeignKey(Employee,related_name="attendances",on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.TextField(choices=STATUS.choices,default = 0)
    

class LogType(models.TextChoices):
    LOGIN = "CHECK-IN"
    LOGOUT= "CHECK-OUT"


class AttendanceLog(models.Model):
    attendance = models.ForeignKey(Attendance,related_name="logs",on_delete=models.CASCADE)
    type = models.TextField(choices=LogType.choices,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
