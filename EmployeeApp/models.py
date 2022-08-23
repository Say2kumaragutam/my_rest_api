from django.db import models

# Create your models here.
class Departments(models.Model):
    Department_id=models.AutoField(primary_key=True)
    Department_name=models.CharField(max_length=500)

class Employee(models.Model):
    Employee_id=models.AutoField(primary_key=True)
    Employee_name=models.CharField(max_length=500)
    Department=models.CharField(max_length=500)
    DateOfJoining=models.DateField()
    PhotoFileName=models.CharField(max_length=500)
