from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *

# Create your views here.

def index(request):
    # For Create Employees data 
    if request.method == "POST":
         FirstName = request.POST['fname'].capitalize()
         LastName = request.POST['lname'].capitalize()
         DOB = request.POST['dob']
         Role = request.POST['role'].capitalize()
         PhoneNo = request.POST['num']
         Email = request.POST['mail']
         Address = request.POST['address'].capitalize()
         EmployeeStatus = Employees.objects.filter(EmployeeEmail=Email)
         if EmployeeStatus.exists():
            messages.error(request,"This Employee is already exist!!")
            return redirect('home')
         Employee = Employees(EmployeeFirstName=FirstName,EmployeeLastName=LastName,EmployeeBirthdate=DOB,EmployeeRole=Role,EmployeePhone_No=PhoneNo,EmployeeEmail=Email,EmployeeAddress=Address)
         Employee.save()
         messages.success(request, "Employee has been created!!")
         return redirect('home')
    return render(request, 'ems/index.html')

def manage(request):
    # Render management page of Employees
    Employee = Employees.objects.all()
    return render(request, 'ems/employees.html',{'Employee':Employee})

def delete(request,Id):
    # Delete the employee with their unique Id 
    employee = Employees.objects.filter(id=Id)
    employee.delete()
    messages.success(request, "Employee has been Deleted!!")
    return redirect('management')

def updatePage(request,Id):
    # for render update page with previous value of employees 
    Employee = Employees.objects.filter(id=Id)
    return render(request, 'ems/update.html',{'Employee':Employee})

def update(request,Id):
    # For update Emplaoyees data
    if request.method == 'POST':
        FirstName = request.POST['fname'].capitalize()
        LastName = request.POST['lname'].capitalize()
        DOB = request.POST['dob']
        Role = request.POST['role'].capitalize()
        PhoneNo = request.POST['num']
        Email = request.POST['mail']
        Address = request.POST['address'].capitalize()
        try:
            Employees.objects.filter(id=Id).update(EmployeeFirstName=FirstName,EmployeeLastName=LastName,EmployeeBirthdate=DOB,EmployeeRole=Role,EmployeePhone_No=PhoneNo,EmployeeEmail=Email,EmployeeAddress=Address)
            messages.success(request, f"Employee {FirstName}'s data has been  updated successflly!!")
            return redirect('updateEmployee',Id)
        except:
            messages.error(request,'Sorry !! this Email id already exist')
            return redirect('updateEmployee', Id)