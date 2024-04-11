from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from pagina.models import Materi,Careers, students, Teacher
from .forms import MateriForm, CareersForm, StudentsForm, TeacherForm, RegisterForm
from django.contrib import messages
from django.urls import path
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
#Importamos el decorador que bloqueara las vistas para que solo las pueda ver el administrador
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

# Vista para la página de inicio

# Esta función maneja el registro de nuevos usuarios.
def register(request):
    # Se instancia un formulario de registro.
    register_form = RegisterForm()
    # Si el método de la solicitud es POST, es decir, se está enviando un formulario.
    if request.method == 'POST':
        # Se crea una instancia del formulario de registro con los datos recibidos.
        register_form = RegisterForm(request.POST)
        # Si el formulario es válido.
        if register_form.is_valid():
            # Se guarda el usuario en la base de datos.
            register_form.save()
            # Se muestra un mensaje de éxito.
            messages.success(request, "¡El usuario se ha registrado exitosamente!")
            # Se redirige al usuario a la página de inicio.
            return redirect('index')
    # Se renderiza el formulario de registro.
    return render(request, 'users/register.html', {
        'title': 'Crear cuenta',
        'register': register_form
    })

# Esta función maneja el inicio de sesión de usuarios.
def login_user(request):
    # Si la solicitud es de tipo POST.
    if request.method == "POST":
        # Se obtienen el nombre de usuario y la contraseña del formulario.
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Se autentica al usuario.
        user = authenticate(request, username=username, password=password)
        # Si el usuario es autenticado correctamente.
        if user is not None:
            # Se inicia la sesión del usuario.
            login(request, user)
            # Se redirige al usuario a la página de inicio.
            return redirect("index")
        # Si la autenticación falla.
        else:
            # Se muestra un mensaje de advertencia.
            messages.warning(request, "El nombre usuario y/o contraseña no válidos")
    # Se renderiza el formulario de inicio de sesión.
    return render(request, 'users/login.html')

# Esta función maneja el cierre de sesión de usuarios.
def logout_user(request):
    # Se cierra la sesión del usuario.
    logout(request)
    # Se redirige al usuario a la página de inicio de sesión.
    return redirect('login')
#--------------------------------------------------------------------------------------------------------------------
# Esta función maneja la vista de la página de inicio.
def index(request):
    # Retorna la plantilla 'index.html' renderizada junto con algunos datos adicionales.
    return render(request, 'nav/index.html', {
        'my_variable': 'soy un dato que está en la vista',
        'title': 'Inicio del sitio',
        'titulo': 'Página de Inicio',
    })

# Esta función maneja la vista para la página futura (future).
def future(request):
    # Retorna la plantilla 'future.html' renderizada.
    return render(request, 'nav/future.html')


#--------------------------------------------------------------------------------------------------------------------

# Esta función maneja la vista de la página de carreras.
def careers(request):
    # Obtiene todas las carreras ordenadas por el código.
    career = Careers.objects.order_by('code')
    # Retorna la plantilla 'careers.html' renderizada con la información de las carreras.
    return render(request, 'nav/careers.html', {
        'career': career
    })

# Esta función maneja la vista para editar una carrera específica.
def edit_careers(request, code):
    # Obtiene la carrera específica por su código.
    career = Careers.objects.filter(pk=code).first()
    # Instancia un formulario de carreras con la información de la carrera para editar.
    form = CareersForm(instance=career)
    # Retorna la plantilla 'edit/career.html' renderizada con el formulario y la información de la carrera.
    return render(request, 'edit/career.html', {'form': form, 'career': career})

# Esta función maneja la actualización de una carrera específica.
def update_careers(request, code):
    # Obtiene la carrera específica por su código.
    career = Careers.objects.get(pk=code)
    # Instancia un formulario de carreras con los datos recibidos en la solicitud y la información de la carrera a actualizar.
    form = CareersForm(request.POST, instance=career)
    # Si el formulario es válido.
    if form.is_valid():
        # Guarda los cambios en la carrera.
        form.save()
    # Obtiene todas las carreras ordenadas por el código.
    career = Careers.objects.order_by('code')
    # Retorna la plantilla 'nav/careers.html' renderizada con la lista actualizada de carreras.
    return render(request, 'nav/careers.html', {'career': career})

# Esta función maneja la eliminación de una carrera específica.
def eliminarCareers(request, code):
    # Obtener la carrera por su ID.
    carrera = Careers.objects.get(id=code)
    
    # Verificar si la carrera existe.
    if carrera:
        # Eliminar la carrera.
        carrera.delete()
        # Redireccionar a la página de carreras después de eliminar.
        return redirect('careers')
    else:
        # Manejar el caso donde la carrera no existe.
        return render(request, 'nav/careers.html', {'message': 'Carrera no encontrada'})

# Esta función maneja la creación de una nueva carrera.
@user_passes_test(lambda u: u.is_superuser)
def create_career(request):
    # Si la solicitud es de tipo POST.
    if request.method == 'POST':
        # Se instancia un formulario de carreras con los datos recibidos en la solicitud.
        form = CareersForm(request.POST)
        # Si el formulario es válido.
        if form.is_valid():
            # Guarda la nueva carrera.
            form.save()
            # Muestra un mensaje de éxito.
            messages.success(request, "Carrera agregada correctamente!")
            # Redirecciona a la página de carreras después de agregar la carrera.
            return redirect('careers')
    # Si la solicitud no es de tipo POST o el formulario no es válido, se instancia un formulario vacío.
    else:
        form = CareersForm()
    # Retorna la plantilla 'forms/create_career.html' renderizada con el formulario de creación de carrera.
    return render(request, 'forms/create_career.html', {'form': form, 'messages': messages.get_messages(request)})


#--------------------------------------------------------------------------------------------------------------------

# Esta función maneja la vista de la página de cursos.
def courses(request):
    # Obtiene todas las materias ordenadas por el código.
    materi = Materi.objects.order_by('code')
    # Retorna la plantilla 'courses.html' renderizada con la información de las materias.
    return render(request, 'nav/courses.html', {
        'materi': materi
    })

# Esta función maneja la vista para editar un curso específico.
def edit_courses(request, code):
    # Obtiene el curso específico por su código.
    course = Materi.objects.filter(pk=code).first()
    # Instancia un formulario de materia con la información del curso para editar.
    form = MateriForm(instance=course)
    # Retorna la plantilla 'edit/course.html' renderizada con el formulario y la información del curso.
    return render(request, 'edit/course.html', {'form': form, 'course': course})

# Esta función maneja la actualización de un curso específico.
def update_courses(request, code):
    # Obtiene el curso específico por su código.
    course = Materi.objects.filter(pk=code).first()
    # Instancia un formulario de materia con los datos recibidos en la solicitud y la información del curso a actualizar.
    form = MateriForm(request.POST, instance=course)
    # Si el formulario es válido.
    if form.is_valid():
        # Guarda los cambios en el curso.
        form.save()
    # Obtiene todas las materias ordenadas por el código.
    course = Materi.objects.order_by('code')
    # Retorna la plantilla 'nav/courses.html' renderizada con la lista actualizada de cursos.
    return render(request, 'nav/courses.html', {'course': course})

# Esta función maneja la eliminación de un curso específico.
def eliminarMateria(request, code):
    # Obtener la materia por su ID.
    materia = Materi.objects.get(pk=code)
    
    # Verificar si la materia existe.
    if materia:
        # Eliminar la materia.
        materia.delete()
        # Redireccionar a la página de materias después de eliminar.
        return redirect('courses')
    else:
        # Manejar el caso donde la materia no existe.
        return render(request, 'nav/courses.html', {'message': 'Materia no encontrada'})

# Esta función maneja la creación de una nueva materia.
def create_materi(request):
    # Si la solicitud es de tipo POST.
    if request.method == 'POST':
        # Se instancia un formulario de materia con los datos recibidos en la solicitud.
        form = MateriForm(request.POST)
        # Si el formulario es válido.
        if form.is_valid():
            # Guarda la nueva materia.
            form.save()
            # Muestra un mensaje de éxito.
            messages.success(request, "Materia agregada correctamente!")
            # Redirecciona a la página de cursos después de agregar la materia.
            return redirect('courses')
    # Si la solicitud no es de tipo POST o el formulario no es válido, se instancia un formulario vacío.
    else:
        form = MateriForm()
    # Retorna la plantilla 'forms/create_materi.html' renderizada con el formulario de creación de materia.
    return render(request, 'forms/create_materi.html', {'form': form})
#--------------------------------------------------------------------------------------------------------------------

# Esta función maneja la vista de la página de estudiantes.
def student(request):
    # Obtiene todos los estudiantes.
    students_list = students.objects.all()
    # Retorna la plantilla 'students.html' renderizada con la información de los estudiantes.
    return render(request, 'nav/students.html', {'students': students_list})

# Esta función maneja la vista para editar un estudiante específico.
def edit_student(request, code):
    # Obtiene el estudiante específico por su código.
    student = students.objects.filter(pk=code).first()
    # Instancia un formulario de estudiantes con la información del estudiante para editar.
    form = StudentsForm(instance=student)
    # Retorna la plantilla 'edit/student.html' renderizada con el formulario y la información del estudiante.
    return render(request, 'edit/student.html', {'form': form, 'student': student})

# Esta función maneja la actualización de un estudiante específico.
def update_student(request, code):
    # Obtiene el estudiante específico por su código.
    student = students.objects.filter(pk=code).first()
    # Instancia un formulario de estudiantes con los datos recibidos en la solicitud y la información del estudiante a actualizar.
    form = StudentsForm(request.POST, request.FILES, instance=student)
    # Si el formulario es válido.
    if form.is_valid():
        # Guarda los cambios en el estudiante.
        form.save()
    # Obtiene todos los estudiantes ordenados por el código.
    student = students.objects.order_by('code')
    # Retorna la plantilla 'nav/student.html' renderizada con la lista actualizada de estudiantes.
    return render(request, 'nav/student.html', {'student': student})

# Esta función maneja la eliminación de un estudiante específico.
def eliminarEstudiante(request, code):
    # Obtener el estudiante por su ID.
    estudiante = students.objects.get(pk=code)
    
    # Verificar si el estudiante existe.
    if estudiante:
        # Eliminar el estudiante.
        estudiante.delete()
        # Redireccionar a la página de estudiantes después de eliminar.
        return redirect('students')
    else:
        # Manejar el caso donde el estudiante no existe.
        return render(request, 'nav/student.html', {'message': 'Estudiante no encontrado'})

# Esta función maneja la creación de un nuevo estudiante.
def create_student(request):
    # Si la solicitud es de tipo POST.
    if request.method == 'POST':
        # Se instancia un formulario de estudiantes con los datos recibidos en la solicitud.
        form = StudentsForm(request.POST, request.FILES)
        # Si el formulario es válido.
        if form.is_valid():
            # Guarda el nuevo estudiante.
            form.save()
            # Muestra un mensaje de éxito.
            messages.success(request, "Estudiante agregado correctamente!")
            # Redirecciona a la página de estudiantes después de agregar el estudiante.
            return redirect('students')
    # Si la solicitud no es de tipo POST o el formulario no es válido, se instancia un formulario vacío.
    else:
        form = StudentsForm()
    # Retorna la plantilla 'forms/create_student.html' renderizada con el formulario de creación de estudiante.
    return render(request, 'forms/create_student.html', {'form': form})

#--------------------------------------------------------------------------------------------------------------------

# Esta función maneja la vista de la página de maestros.
def teachers(request):
    # Obtiene todos los maestros ordenados por el código.
    teachers = Teacher.objects.order_by('code')
    # Retorna la plantilla 'teachers.html' renderizada con la información de los maestros.
    return render(request, 'nav/teachers.html', {
        'teachers': teachers
    })

# Esta función maneja la vista para editar un maestro específico.
def edit_teachers(request, code):
    # Obtiene el maestro específico por su código.
    teacher = Teacher.objects.filter(pk=code).first()
    # Instancia un formulario de maestro con la información del maestro para editar.
    form = TeacherForm(instance=teacher)
    # Retorna la plantilla 'edit/teacher.html' renderizada con el formulario y la información del maestro.
    return render(request, 'edit/teacher.html', {'form': form, 'teacher': teacher})

# Esta función maneja la actualización de un maestro específico.
def update_teacher(request, code):
    # Obtiene el maestro específico por su código.
    teacher = Teacher.objects.filter(pk=code).first()
    # Instancia un formulario de maestro con los datos recibidos en la solicitud y la información del maestro a actualizar.
    form = TeacherForm(request.POST, request.FILES, instance=teacher)
    # Si el formulario es válido.
    if form.is_valid():
        # Guarda los cambios en el maestro.
        form.save()
    # Obtiene todos los maestros ordenados por el código.
    teacher = Teacher.objects.order_by('code')
    # Retorna la plantilla 'nav/teacher.html' renderizada con la lista actualizada de maestros.
    return render(request, 'nav/teacher.html', {'teacher': teacher})

# Esta función maneja la eliminación de un maestro específico.
def eliminarMaestro(request, code):
    # Obtener el maestro por su ID.
    maestro = Teacher.objects.get(pk=code)
    
    # Verificar si el maestro existe.
    if maestro:
        # Eliminar el maestro.
        maestro.delete()
        # Redireccionar a la página de maestros después de eliminar.
        return redirect('teachers')
    else:
        # Manejar el caso donde el maestro no existe.
        return render(request, 'nav/teachers.html', {'message': 'Maestro no encontrado'})

# Esta función maneja la creación de un nuevo maestro.
def create_teacher(request):
    # Si la solicitud es de tipo POST.
    if request.method == 'POST':
        # Se instancia un formulario de maestro con los datos recibidos en la solicitud.
        form = TeacherForm(request.POST, request.FILES)
        # Si el formulario es válido.
        if form.is_valid():
            # Guarda el nuevo maestro.
            form.save()
            # Redirecciona a la página de maestros después de agregar el maestro.
            return redirect('teachers')
    # Si la solicitud no es de tipo POST o el formulario no es válido, se instancia un formulario vacío.
    else:
        form = TeacherForm()
    # Retorna la plantilla 'forms/create_teacher.html' renderizada con el formulario de creación de maestro.
    return render(request, 'forms/create_teacher.html', {'form': form})


#--------------------------------------------------------------------------------------------------------------------