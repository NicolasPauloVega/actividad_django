from django.shortcuts import redirect, render, HttpResponse
from pagina.models import Materi,Careers, students, Teacher
from .forms import MateriForm, CareersForm, StudentsForm, TeacherForm
from django.contrib import messages
from django.urls import path
from . import views

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


def edit_careers(request, code):
    career = Careers.objects.filter(pk=code).first()
    form = CareersForm(instance=career)
    return render(request, 'edit/career.html', {'form': form, 'career': career})


# Funcion del boton de eliminar    
def eliminarCareers(request, id):
    # Obtener la carrera por su ID
    carrera = Careers.objects.get(id=id)
    
    # Verificar si la carrera existe
    if carrera:
        # Eliminar la carrera
        carrera.delete()
        # Redireccionar a la página de carreras después de eliminar
        return redirect('careers')
    else:
        # Manejar el caso donde la carrera no existe
        return render(request, 'error.html', {'message': 'Carrera no encontrada'})

def courses(request):
    materi = Materi.objects.order_by('code')
    return render(request, 'nav/courses.html',{
        'materi': materi
    })
    
def eliminarMateria(request, id):
    # Obtener la materia por su ID
    materia = Materi.objects.get(id=id)
    
    # Verificar si la materia existe
    if materia:
        # Eliminar la materia
        materia.delete()
        # Redireccionar a la página de materias después de eliminar
        return redirect('materias')
    else:
        # Manejar el caso donde la materia no existe
        return render(request, 'error.html', {'message': 'Materia no encontrada'})
        
def student(request):
    students_list = students.objects.all()
    return render(request, 'nav/students.html', {'students': students_list})

def eliminarEstudiante(request, id):
    # Obtener el estudiante por su ID
    estudiante = students.objects.get(id=id)
    
    # Verificar si el estudiante existe
    if estudiante:
        # Eliminar el estudiante
        estudiante.delete()
        # Redireccionar a la página de estudiantes después de eliminar
        return redirect('students')
    else:
        # Manejar el caso donde el estudiante no existe
        return render(request, 'error.html', {'message': 'Estudiante no encontrado'})

def teachers(request):
    teacher = Teacher.objects.order_by('code')
    return render(request, 'nav/teachers.html', {
        'teacher': teacher
    })
    
def eliminarMaestro(request, id):
    # Obtener el maestro por su ID
    maestro = Teacher.objects.get(id=id)
    
    # Verificar si el maestro existe
    if maestro:
        # Eliminar el maestro
        maestro.delete()
        # Redireccionar a la página de maestros después de eliminar
        return redirect('teachers')
    else:
        # Manejar el caso donde el maestro no existe
        return render(request, 'error.html', {'message': 'Maestro no encontrado'})

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

