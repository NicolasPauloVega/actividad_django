from django.shortcuts import render, HttpResponse
from pagina.models import Materi,Careers, students, Teacher

# Create your views here.

# Vista para la página de inicio
def index(request):
    # Retorna la plantilla 'index.html' renderizada junto con algunos datos adicionales
    return render(request, 'index.html', {
        'my_variable': 'soy un dato que esta en la vista',
        'title': 'Inicio del sitio',
        'titulo': 'Página de Inicio',
    })

# Vista para la página futura (future)
def future(request):
    # Retorna la plantilla 'future.html' renderizada
    return render(request, 'future.html')

# Vista para los programas académicos
def careers(request):
    career = Careers.objects.order_by('code')
    # Retorna la plantilla 'careers.html' renderizada
    return render(request, 'careers.html',{
        'career': career
    })

def courses(request):
    materi = Materi.objects.order_by('code')
    return render(request, 'courses.html',{
        'materi': materi
    })

def student(request):
    student = students.objects.order_by('code')
    return render(request, 'students.html',{
        'student': student
    })

def teachers(request):
    teacher = Teacher.objects.order_by('code')
    return render(request, 'teachers.html', {
        'teacher': teacher
    })
    