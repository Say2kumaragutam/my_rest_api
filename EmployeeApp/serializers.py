from rest_framework import serializers
from EmployeeApp.models import Departments, Employee


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields=('Department_id','Department_name')
    
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=('Employee_id','Employee_name','Department','DateOfJoining','PhotoFileName')