from api.models import Employee , CURRENT_USER_MODEL



class EmployeeService():
    def create_employee(data:dict) -> Employee:
        user = CURRENT_USER_MODEL.objects.create_user(**data)
        employee = Employee.objects.create(user = user)
        return employee

    def get_employee_by_id(id:int) -> Employee:
        employee = Employee.objects.filter(user__id = id).get()
        return employee

    def update_employee(obj:Employee,data:dict) -> Employee:
        for k,v in data.items():
            if getattr(obj,k) != v :
                setattr(obj,k,v)

        obj.save()
        return obj