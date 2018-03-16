"""
Versão homologada no django 2.0.3 + python3 com virtualenv
Listar usuario via API: http://127.0.0.1:8000/employee/
Add usuário via API, segue exemplo:  http://127.0.0.1:8000/employee/add?name=caroline&email=caroline@bp.com.br&departament=conteudo
Remove usuário via API, segue exemplo: http://127.0.0.1:8000/employee/remove?id=1

Fiz a passagem de parametro diferente da função remove e add_eployee propositalmente para mostrar os dois jeitos.

############## Informações ###################
Autor: Flavio Guilherme Rocha da Silva
Email: flaviog.info@gmail.com
"""
from django.shortcuts import render, redirect
from employees.models import Employee
from django.http import JsonResponse
from .forms import EmployeeRegisterForm
from .forms import FilterForm
from django.http import *
from django.contrib import messages

#Função index. Irá rendereziar a pagina inicial
def index(request):
	#Pegar todos os funcionarios para listar na tela
	employees = Employee.objects.all()
	if request.method == 'POST':
		form = FilterForm(request.POST)
		#Quando for clicar no botão de filtrar realizar a ação de filter igual LIKE do SQL
		if 'submit' in request.POST and form.is_valid():
			employees = Employee.objects.filter(name__contains=form.cleaned_data['fieldFilter'])
	else:
		form = FilterForm()

	return render(request, 'index.html', {'employees' : employees, 'title':'Employee\'s Panel', 'form':form})

#função de serviço para adicionar usuario, passagem de parametro pela URL utilizando a request.GET.get
def add_employee(request):
	employee_name = request.GET.get('name', '')
	employee_email = request.GET.get('email','')
	employee_departament = request.GET.get('departament','')
	#salvando no banco de dados
	Employee(name=employee_name, email=employee_email, departament=employee_departament).save()
	return redirect('employees')

#Função para o serviço de remoção, agora definido parametro no arquivo urls.py e passando o ID do usuário que quer deletar
def remove_employee(request, employee_id):
	Employee.objects.get(id=employee_id).delete()
	return redirect('employees')

#Função para disponibilizar via serviço a lista de Usuários em json
def list_employee(request):
	employees = Employee.objects.all().values('name', 'email', 'departament')
	employees_list = list(employees)
	return JsonResponse(employees_list, safe=False)

"""Função que renderizarar a pagina de cadastro de funcionario e aproveitei para usar para alteração de usuário
mais uma vez usando o request.GET.get"""
def register_employee(request):
	employee_id = request.GET.get('id', '')

	#Caso o Id for passado por parametro instanciar o Objeto Employee para carregar no form
	if employee_id:
		employee_alter = Employee.objects.get(id=employee_id)

	if request.method == 'POST':
		form = EmployeeRegisterForm(request.POST)
		if form.is_valid():
			if employee_id:
				employee_alter.name = form.cleaned_data['name']
				employee_alter.email = form.cleaned_data['email']
				employee_alter.departament = form.cleaned_data['departament']
				employee_alter.save()
			else:
				#Salvando um novo registro caso não tenha passado nenhum ID como parametro comprovando que então é um novo usuário a ser cadastrado
				form.save()
				messages.success(request, ('Nice'))
			return redirect('employees')
	else:
		if employee_id:
			#Carregando as informações do Employee que será alterado
			form = EmployeeRegisterForm(initial={'name': employee_alter.name, 'email': employee_alter.email, 'departament':employee_alter.departament})
		else:
			form = EmployeeRegisterForm()
			
	return render(request, 'register.html', {'title':'Employee Register', 'form':form})