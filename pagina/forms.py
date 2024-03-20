from django import forms
from .models import Materi, Careers, students, Teacher

class MateriForm(forms.ModelForm):
    class Meta:
        model = Materi
        fields = ['name', 'description', 'creadits']

class CareersForm(forms.ModelForm):
    class Meta:
        model = Careers
        fields = '__all__'

class StudentsForm(forms.ModelForm):
    class Meta:
        model = students
        fields = ['name', 'last_name', 'email', 'phone']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'correo', 'carrera', 'materias_imp']

        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }