from django import forms
from .models import Materi, Careers, students, Teacher

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MateriForm(forms.ModelForm):
    # Define un formulario utilizando el modelo Materi.
    class Meta:
        # Asocia el formulario con el modelo Materi.
        model = Materi
        # Define los campos del modelo que estarán presentes en el formulario.
        fields = ['name', 'description', 'credits']
        # Define nombres personalizados para cada campo del formulario.
        labels = {
            'name': 'Nombre',
            'description': 'Descripción',
            'credits': 'Créditos'
        }
        # Asigna widgets personalizados para cada campo del formulario, que controlan su apariencia y comportamiento.
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
            'credits': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Créditos'}),
        }

class CareersForm(forms.ModelForm):
    # Define un formulario utilizando el modelo Careers.
    class Meta:
        # Asocia el formulario con el modelo Careers.
        model = Careers
        # Define los campos del modelo que estarán presentes en el formulario.
        fields = ['name', 'duration']
        # Define nombres personalizados para cada campo del formulario.
        labels = {
            'name': 'Nombre',
            'duration': 'Duración'
        }
        # Asigna widgets personalizados para cada campo del formulario, que controlan su apariencia y comportamiento.
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Duración'})
        }

class StudentsForm(forms.ModelForm):
    # Define un formulario utilizando el modelo students.
    class Meta:
        # Asocia el formulario con el modelo students.
        model = students
        # Define los campos del modelo que estarán presentes en el formulario.
        fields = ['name', 'last_name', 'email', 'phone', 'photo', 'date_of_birth']
        # Define nombres personalizados para cada campo del formulario.
        labels = {
            'name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
            'phone': 'Teléfono',
            'date_of_birth': 'Fecha de nacimiento'
        }
        # Asigna widgets personalizados para cada campo del formulario, que controlan su apariencia y comportamiento.
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control-file'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'last_name', 'email', 'phone', 'photo', 'date_of_birth']
        #Nombre personalizado para cada campo del formulario
        labels = {
            'name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electronico',
            'phone': 'Telefono',
            'photo': 'Foto',
            'date_of_birth': 'Fecha de nacimiento'
        }
        #Le asignamos un widget personalizado para cada campo del formulario
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control-file'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }

#formulario para el registro de usario
class RegisterForm(UserCreationForm):
    # Define un formulario de registro de usuario que hereda de UserCreationForm.
    class Meta:
        # Asocia el formulario con el modelo User.
        model = User
        # Define los campos del modelo que estarán presentes en el formulario.
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
