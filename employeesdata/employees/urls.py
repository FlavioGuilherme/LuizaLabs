from django.urls import path, re_path

from . import views

urlpatterns = [
	path('employees_panel/', views.index, name='employees'),
	path('employee/add', views.add_employee, name='add'),
	re_path(r'^employee/remove\?id=(?P<employee_id>\d+)$', views.remove_employee, name='remove'),
	path('employee/', views.list_employee, name='list'),
	path('register/', views.register_employee, name='register')
]