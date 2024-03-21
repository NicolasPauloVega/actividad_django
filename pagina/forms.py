from django import forms
from .models import Materi, Careers, students, Teacher

class MateriForm(forms.ModelForm):
    class Meta:
        model = Materi
        fields = ['name', 'description', 'credits']
        #Nombre personalizado para cada campo del formulario
        labels = {
            'name': 'Nombre',
            'description': 'Descripcion',
            'credits': 'Creditos'
        }
        #Le asignamos un widget personalizado para cada campo del formulario
        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
        'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
        'credits': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Créditos'}),
        }

class CareersForm(forms.ModelForm):
    class Meta:
        model = Careers
        fields = ['name', 'duration']
        #Nombre personalizado para cada campo del formulario
        labels = {
            'name': 'Nombre',
            'duration': 'Duracion'
        }
        #Le asignamos un widget personalizado para cada campo del formulario
        widgets= {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Duracion'})
        }

class StudentsForm(forms.ModelForm):
    class Meta:
        model = students
        fields = ['name', 'last_name', 'email', 'phone', 'photo', 'date_of_birth']
        #Nombre personalizado para cada campo del formulario
        labels = {
            'name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electronico',
            'phone': 'Telefono',
            'date_of_birth': 'Fecha de nacimiento'
        }
        #Le asignamos un widget personalizado para cada campo del formulario
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'las_name': forms.TextInput(attrs={'class': 'form-control'}),
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
            'last_name': 'apellido',
            'email': 'Correo electronico',
            'phone': 'Telefono',
            'photo': 'Foto',
            'date_of_birth': 'Fecha de nacimiento'
        }
        #Le asignamos un widget personalizado para cada campo del formulario
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'las_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control-file'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }