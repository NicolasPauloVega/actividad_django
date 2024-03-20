from django import forms
from .models import Materi, Careers, students, Teacher

class MateriForm(forms.ModelForm):
    class Meta:
        model = Materi
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

class CareersForm(forms.ModelForm):
    class Meta:
        model = Careers
        fields = '__all__'

class StudentsForm(forms.ModelForm):
    class Meta:
        model = students
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }



