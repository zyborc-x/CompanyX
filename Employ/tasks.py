import os
import django
from celery import shared_task, Celery
from .models import Employee
from .serializers import EmployeeSerializer

# Django settings initialization
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CompanyX.settings')
django.setup()


# Task: Create an Employee
@shared_task
def create_employee_task(data):
    print(data)
    serializer = EmployeeSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return {"status": "success", "message": "Employee created successfully."}
    return {"status": "error", "errors": serializer.errors}

    
@shared_task
def put_employee_task(task_data):
    employee_id = task_data.get('id')
    employee_data = task_data.get('data')
    employ = Employee.objects.get(pk= employee_id)
    print(employ)
    serializer = EmployeeSerializer(employ, data =employee_data, partial = True)
    if serializer.is_valid():
        serializer.save()
    return {"status": "success", "message": "Employee created successfully."}

@shared_task
def delete_employee_task(task_data):
    employee_id = task_data.get('id')
    employ = Employee.objects.get(pk= employee_id)
    employ.delete()
    return {"status": "success", "message": "Employee deleted successfully."}