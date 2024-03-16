from django.db import models

# Create your models here.

class Materi(models.Model):
    code = models.AutoField(primary_key=True, default=1, verbose_name="codigo")
    name = models.CharField(max_length=150, verbose_name="nombre")
    description = models.TextField(verbose_name="descripcion")
    credits = models.IntegerField(verbose_name="creditos")
    Creation_date = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación")
    update_date = models.DateField(auto_now=True, verbose_name="fecha de actualización")
    class Meta:
        #db_table=""
        verbose_name="Materia"
        verbose_name="Materias"