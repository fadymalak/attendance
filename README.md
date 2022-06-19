# Simple attendance API


## DB Model

Employee model
used custom Employee model to add more fields to it for later development instead of use User model directly
```python
class Employee(models.Model):
    user = models.OneToOneField(User,related_name="employee",on_delete=models.CASCADE)
```

Attendance model 
contain days these attended by Employee
```python
class Attendance(models.Model):
    employee = models.ForeignKey(Employee,related_name="attendances",on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS.choices,default = 0)
```

AttendanceLog model
contain time & date when Employee check-in & checkout 
support multiply check-in & check-out for same day ( Bouns 1 )
```python
class AttendanceLog(models.Model):
    attendance = models.ForeignKey(Attendance,related_name="logs",on_delete=models.CASCADE)
    type = models.TextField(choices=LogType.choices,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
```


## installation

### Install Dependencies
using pip 
```bash
pip install -r requirements.txt
```

### Create migration & DB (SQLite)
```bash
python manage.py createmigrations
python manage.py migrate
```


## How to Run 
```bash
python manage.py runserver
```