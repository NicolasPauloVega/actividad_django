"""
URL configuration for School project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
# from pagina import views
import pagina.views # Importa las vistas desde la aplicación 'pagina'
from django.conf import settings

# Definición de las URL de la aplicación
urlpatterns = [
    # URL para la página de inicio, que llama a la vista 'index' definida en 'pagina.views'
    path('', pagina.views.index, name="index"),
    # URL para la página futura, que llama a la vista 'future' definida en 'pagina.views'
    path('future/', pagina.views.future, name="future"),
    # URL para la página de programas académicos, que llama a la vista 'careers' definida en 'pagina.views'
    path('carreras/', pagina.views.careers, name="careers"),
    #URL para la pagina de estudiantes, que llama a la vista 'students' definida en 'pagina.views'
    path('estudiantes/', pagina.views.student, name="students"),
    #URL para la pagina de maestros, que llama a la vista 'teachers' definida en 'pagina.views'
    path('maestros/', pagina.views.teachers, name="teachers"),
    #URL para la pagina de materias, que llama a la vista 'courses' definida en 'pagina.views'
    path('materias/', pagina.views.courses, name="courses"),
    
 # URLs de los formularios creados 
    path('agregar-materia/', pagina.views.create_materi, name='create_materi'),
    path('agregar-carrera/', pagina.views.create_career, name='create_career'),
    path('agregar-estudiante/', pagina.views.create_student, name='create_student'),
    path('agregar-maestro/', pagina.views.create_teacher, name='create_teacher'),
    
    #Urls de edicion
    path('editar-carrera/<int:code>/', pagina.views.edit_careers, name='edit_career'),
    path('editar-materia/<int:code>/', pagina.views.edit_courses, name='edit_course'),
    path('editar-estudinte/<int:code>/', pagina.views.edit_student, name='edit_student'),
    path('editar-maestro/<int:code>/', pagina.views.edit_teachers, name='edit_teacher'),

    #URLs de actualizacion
    path('actualizar-carrera/<int:code>/', pagina.views.update_careers, name='update_career'),
    path('actualizar-materia/<int:code>/', pagina.views.update_courses, name='update_course'),
    path('actualizar-estudiante/<int:code>/', pagina.views.update_student, name='update_student'),
    path('actualizar-maestro/<int:code>/', pagina.views.update_teacher, name='update_teacher'),

    #URLs de eliminar
    path('eliminar-carrera/<int:code>/', pagina.views.eliminarCareers, name="delete_careers"),
    path('eliminar-materia/<int:code>/', pagina.views.eliminarMateria, name="delete_matery"),
    path('eliminar-estudiante/<int:code>/', pagina.views.eliminarEstudiante, name="delete_student"),
    path('eliminar-maestro/<int:code>/', pagina.views.eliminarMaestro, name="delete_teacher"),

    #URLs para login y registrer de django
    path('registro/', pagina.views.register, name="register"),
    path('iniciar-sesion/', pagina.views.login, name="login"),
    path('cerrar-sesion/', pagina.views.logout, name="logout"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)