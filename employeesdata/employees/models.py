from django.db import models
from django.contrib.auth.models import User

#Classe de funcionario para a criação no banco de dados
class Employee(models.Model):
	name = models.CharField(max_length=255, null=False)
	email = models.CharField(max_length=255, null=False)
	departament = models.CharField(max_length=50, null=False)