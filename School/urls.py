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
from django.contrib import admin
from django.urls import path, include
# from pagina import views
import pagina.views # Importa las vistas desde la aplicación 'pagina'
from django.conf import settings

# Definición de las URL de la aplicación
urlpatterns = [
    # URL para acceder al panel de administración de Django
    path('admin/', admin.site.urls),
    # URL para la página de inicio, que llama a la vista 'index' definida en 'pagina.views'
    path('', pagina.views.index, name="index"),
    # URL para la página futura, que llama a la vista 'future' definida en 'pagina.views'
    path('future/', pagina.views.future, name="future"),
    # URL para la página de programas académicos, que llama a la vista 'careers' definida en 'pagina.views'
    path('carreras/', pagina.views.careers, name="careers"),
    #URL para la pagina de estudiantes, que llama a la vista 'students' definida en 'pagina.views'
    path('estudiantes/', pagina.views.student, name="students"),
    #URL para la pagina de maestros, que llama a la vista 'teachers' definida en 'pagina.views'
    path('profesores/', pagina.views.teachers, name="teachers"),
    #URL para la pagina de materias, que llama a la vista 'courses' definida en 'pagina.views'
    path('materias/', pagina.views.courses, name="courses"),
    
 # URLs de los formularios creados 
    path('create/materi/', pagina.views.create_materi, name='create_materi'),
    path('create/career/', pagina.views.create_career, name='create_career'),
    path('create/student/', pagina.views.create_student, name='create_student'),
    path('create/teacher/', pagina.views.create_teacher, name='create_teacher'),
    
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)