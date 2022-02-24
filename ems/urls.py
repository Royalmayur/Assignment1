from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('manageEmployees', views.manage, name='management'),
    path('manageEmployees/deleteEmployees/<Id>', views.delete, name='delEmployee'),
    path('manageEmployees/UpadateEmployees/<Id>', views.updatePage, name='updateEmployee'),
    path('manageEmployees/updateEmployees/update/<Id>', views.update, name='update'),
]