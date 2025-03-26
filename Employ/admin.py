from django.contrib import admin
from . models import *

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name' , 'last_name' , 'email' , 'phone', 'department']
    
    
@admin.register(Details)
class DetailsAdmin(admin.ModelAdmin):
    list_display = ['id' , 'tech' , 'experience' , 'age']