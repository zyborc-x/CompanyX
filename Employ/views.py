from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from . models import *
from . serializers import *
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from .tasks import create_employee_task , put_employee_task, delete_employee_task


class EmployeeAPI(APIView):
    def get(self, request, pk=None):
        if pk:
            return Response({"task_id":" task.id", "status": "Fetching employee in progress."})
        else:
            print("a")
            emp = Employee.objects.all()
            paginator = LimitOffsetPagination()
            paginator.default_limit = 10
            result_page = paginator.paginate_queryset(emp, request)
            serializer = EmployeeSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        

    def post(self, request):
        # print(request.data)
        # print(request.data['id'])
        for x in request.data['department']:
            employ_data = { "first_name": request.data['first_name'],  "last_name": request.data['last_name'], "email": request.data['email'], "phone":request.data['phone'], "department" : x}
            create_employ = EmployeeSerializer(data=employ_data)
            if create_employ.is_valid():
                create_employ.save()
            return Response({'msg' : 'Data Created!!'},  status=status.HTTP_201_CREATED)
        
        task = create_employee_task.delay(request.data)
        return Response({"task_id": task.id, "status": "Employee creation is in the progress."})

# =================================================================================================================>
# =================================================================================================================>

#update view Cond. PUT
    def put(self, request, pk, format=None):
        id = pk
        data =  request.data
        task_data = {
        'id': id,
        'data': data
        }
        task = put_employee_task.delay(task_data)
        return Response({"task_id": task.id, "status": "Employee data update is in the progress."})
    
     
#update view Cond. PATCH
    def patch(self, request, pk, format=None):
        id = pk
        print(request)
        employ_data = Employee.objects.get(pk=id)
        serializer = EmployeeSerializer(employ_data, data=request.data , partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Partial Data Updated!!'})
# =================================================================================================================>
# =================================================================================================================>
#Delete view Cond.
    def delete(self, request, pk):
            if request.method == 'DELETE' :
                data =  request.data
                id =pk
                task_data = {
                'id': id
                }
                task = delete_employee_task.delay(task_data)
                return Response({"task_id": task.id, "status": "Employ Data Deleted is in the progress."})
    
# =================================================================================================================>
# =================================================================================================================>


class DetailsAPI(APIView):
    def get(self,request,pk=None):
        if (pk):
            # emp = Employee.objects.get(id=pk)
            dt = get_object_or_404(Details, id=pk)
            print(dt)
            serializer = DetailsSerializer(dt)
            return Response(serializer.data);
        else:
            id = pk
            dt = Details.objects.all()
            paginator = LimitOffsetPagination()
            paginator.default_limit = 10
            result_page = paginator.paginate_queryset(dt, request)
            serializer = DetailsSerializer(result_page, many = True)
            return paginator.get_paginated_response(serializer.data)
        



    def post(self, request):
        # if request.method == 'POST' :
        x = request.data
        serializer = DetailsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data Created!!'},  status=status.HTTP_201_CREATED)
        return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)
    
  
  
    
    def put(self, request, pk, format=None):
        id = pk
        dt = Details.objects.get(pk=id)
        serializer = DetailsSerializer(dt, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Complete Data Updated!!'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  
    def patch(self, request, pk, format=None):
                # print(request)
        id = pk
        print(request)
        dt = Details.objects.get(pk=id)
        serializer = DetailsSerializer(dt, data=request.data , partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Partial Data Updated!!'})
        return Response(serializer.errors)


    def delete(self, request, pk):
        if request.method == 'DELETE' :
            id =pk
            dt = Details.objects.get(pk=id)
            dt.delete()
            return Response({'msg' : 'Data Deleted!!'})