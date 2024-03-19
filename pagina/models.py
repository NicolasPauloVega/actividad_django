from django.db import models

# Create your models here.

class Materi(models.Model):
    # Campo de clave primaria para el modelo Materia, se autoincrementa.
    code = models.AutoField(primary_key=True, default=1, verbose_name="codigo")
    # Campo para el nombre del Materi.
    name = models.CharField(max_length=150, verbose_name="nombre")
    # Campo para la descripción del Materi.
    description = models.TextField(verbose_name="descripcion")
    # Campo para los créditos del Materi.
    credits = models.IntegerField(verbose_name="creditos")
    # Campo para la fecha de creación del Materi, se establece automáticamente con la fecha y hora actual al crear una instancia.
    Creation_date = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación")
    # Campo para la fecha de actualización del Materi, se actualiza automáticamente a la fecha actual cuando se guarda una instancia.
    update_date = models.DateField(auto_now=True, verbose_name="fecha de actualización")

    class Meta:
        # Clase Meta para proporcionar metadatos para el modelo Materia.
        #db_table=""
        # Nombre legible para una instancia única del modelo.
        verbose_name="Materia"
        # Nombre en plural para múltiples instancias del modelo.
        verbose_name="Materias"