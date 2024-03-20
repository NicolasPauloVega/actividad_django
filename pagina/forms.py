from django import forms
from .models import Materi, Careers, students, Teacher

class MateriForm(forms.ModelForm):
    class Meta:
        model = Materi
        fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'profesor']

class CareersForm(forms.ModelForm):
    class Meta:
        model = Careers
        fields = ['nombre', 'descripcion', 'duración', 'tipo']

class StudentsForm(forms.ModelForm):
    class Meta:
        model = students
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'correo', 'carrera']

        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'correo', 'carrera', 'materias_imp']

        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }