from rest_framework import serializers
from . models import *

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta :
        model = Employee
        fields = ['id', 'first_name' , 'last_name' , 'email' , 'phone', 'department']
                                
                                # OR
        

class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = '__all__'