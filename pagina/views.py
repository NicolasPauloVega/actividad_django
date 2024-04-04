from django.shortcuts import redirect, render, HttpResponse
from pagina.models import Materi,Careers, students, Teacher
from .forms import MateriForm, CareersForm, StudentsForm, TeacherForm
from django.contrib import messages

# Create your views here.

# Vista para la página de inicio
def index(request):
    # Retorna la plantilla 'index.html' renderizada junto con algunos datos adicionales
    return render(request, 'nav/index.html', {
        'my_variable': 'soy un dato que esta en la vista',
        'title': 'Inicio del sitio',
        'titulo': 'Página de Inicio',
    })

# Vista para la página futura (future)
def future(request):
    # Retorna la plantilla 'future.html' renderizada
    return render(request, 'nav/future.html')

# Vista para los programas académicos
def careers(request):
    career = Careers.objects.order_by('code')
    # Retorna la plantilla 'careers.html' renderizada
    return render(request, 'nav/careers.html',{
        'career': career
    })

def courses(request):
    materi = Materi.objects.order_by('code')
    return render(request, 'nav/courses.html',{
        'materi': materi
    })

def student(request):
    students_list = students.objects.all()
    return render(request, 'nav/students.html', {'students': students_list})

def teachers(request):
    teacher = Teacher.objects.order_by('code')
    return render(request, 'nav/teachers.html', {
        'teacher': teacher
    })

def create_materi(request):
    if request.method == 'POST':
        form = MateriForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Materia agregada correctamente!")
            return redirect('courses')  # Redirect to courses after successful form submission
    else:
        form = MateriForm()
    return render(request, 'forms/create_materi.html', {'form': form})

def create_career(request):
    if request.method == 'POST':
        form = CareersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Carrera agregada correctamente!")
            return redirect('careers')  # Redirect to careers after successful form submission
    else:
        form = CareersForm()
    return render(request, 'forms/create_career.html', {'form': form, 'messages': messages.get_messages(request)})

def create_student(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Estudiante agregado correctamente!")
            return redirect('students')  # Redirect to students after successful form submission
    else:
        form = StudentsForm()
    return render(request, 'forms/create_student.html', {'form': form})

def create_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('teachers')
    else:
        form = TeacherForm()
    return render(request, 'forms/create_teacher.html', {'form': form})