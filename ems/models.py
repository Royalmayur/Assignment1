from django.db import models

# Create your models here.

class Employees(models.Model):
    EmployeeFirstName = models.CharField(max_length = 150)
    EmployeeLastName = models.CharField(max_length = 150)
    EmployeeBirthdate = models.CharField(max_length = 50)
    EmployeeRole = models.CharField(max_length = 150)
    EmployeePhone_No = models.CharField(max_length = 10)
    EmployeeEmail = models.EmailField(max_length = 254 ,unique=True)
    EmployeeAddress = models.CharField(max_length = 1500)

    def __str__(self):
        return  f'{self.id} - {self.EmployeeFirstName+" "+self.EmployeeLastName}'