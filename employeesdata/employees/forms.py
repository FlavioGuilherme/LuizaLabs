from django import forms
from .models import *

#Forms utilizado no register.html. Utilizei a class ModelForm
class EmployeeRegisterForm(forms.ModelForm):
		class Meta():
			model = Employee
			fields = ['name', 'email', 'departament']

		name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}), required=True, max_length=255)
		email = forms.EmailField(widget=forms.EmailInput(attrs={'class': "form-control"}),required=True, max_length=255)
		departament = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}), required=True, max_length=50)

#form utilizado no index.html. Utilizei a class Form
class FilterForm(forms.Form):
	fieldFilter = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}), max_length=255, label='')



