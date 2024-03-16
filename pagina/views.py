from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html', {
        'my_variable': 'soy un dato que esta en la vista',
        'title': 'Inicio del sitio',
        'titulo': 'Página de Inicio',
    })

def future(request):
    return render(request, 'future.html')

def academic_programs(request):
    return render(request, 'academics_programs.html')