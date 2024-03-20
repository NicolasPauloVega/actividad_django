from django.db import models

# Create your models here.

class Materi(models.Model):
    # Campo de clave primaria para el modelo Materia, se autoincrementa.
    code = models.AutoField(primary_key=True, verbose_name="codigo")
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

    @classmethod
    def get_next_code(cls):
        # Método para obtener el próximo código disponible sumando 1 al código del último registro
        # Ordenamos los registros por código de manera descendente y obtenemos el primer registro
        last_record = cls.objects.order_by('-code').first()
        if last_record:
            # Si hay registros, sumamos 1 al código del último registro
            return last_record.code + 1
        else:
            # Si no hay registros, el próximo código será 1
            return 1

    def save(self, *args, **kwargs):
        # Método para guardar el objeto Materi en la base de datos
        if not self.code:
            # Verificamos si el campo code ya tiene un valor asignado
            # Si no tiene un valor (es decir, es None o no está definido), asignamos el próximo código disponible
            self.code = self.get_next_code()
        # Llamamos al método save de la clase padre para guardar el objeto en la base de datos
        super().save(*args, **kwargs)

class Careers(models.Model):
    # Campo de clave primaria para el modelo carrera, se autoincrementa.
    code = models.AutoField(primary_key=True, verbose_name="codigo")
    # Campo para el nombre del carrera.
    name = models.CharField(max_length=150, verbose_name="nombre")
    # Campo para la duracion de la carrera
    duration = models.PositiveIntegerField(verbose_name="Duracion en la carrera")
    
    class Meta:
        # Clase Meta para proporcionar metadatos para el modelo Materia.
        #db_table=""
        # Nombre legible para una instancia única del modelo.
        verbose_name="Carrera"
        # Nombre en plural para múltiples instancias del modelo.
        verbose_name="Carreras"

    @classmethod
    def get_next_code(cls):
        # Método para obtener el próximo código disponible sumando 1 al código del último registro
        # Ordenamos los registros por código de manera descendente y obtenemos el primer registro
        last_record = cls.objects.order_by('-code').first()
        if last_record:
            # Si hay registros, sumamos 1 al código del último registro
            return last_record.code + 1
        else:
            # Si no hay registros, el próximo código será 1
            return 1

    def save(self, *args, **kwargs):
        # Método para guardar el objeto Materi en la base de datos
        if not self.code:
            # Verificamos si el campo code ya tiene un valor asignado
            # Si no tiene un valor (es decir, es None o no está definido), asignamos el próximo código disponible
            self.code = self.get_next_code()
        # Llamamos al método save de la clase padre para guardar el objeto en la base de datos
        super().save(*args, **kwargs)

class students(models.Model):
    code = models.AutoField(primary_key=True, verbose_name="codigo")
    name = models.CharField(max_length=150, verbose_name="nombre")
    last_name = models.CharField(max_length=150, verbose_name="apellido")
    email = models.EmailField(max_length=254, verbose_name="correo")
    phone = models.CharField(max_length=20, verbose_name="phone")
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    update_date = models.DateField(auto_now=True, verbose_name="fecha de actualizacion")

    class Meta:
        verbose_name="Estudiante"
        verbose_name="Estudiantes"

    @classmethod
    def get_next_code(cls):
        # Método para obtener el próximo código disponible sumando 1 al código del último registro
        # Ordenamos los registros por código de manera descendente y obtenemos el primer registro
        last_record = cls.objects.order_by('-code').first()
        if last_record:
            # Si hay registros, sumamos 1 al código del último registro
            return last_record.code + 1
        else:
            # Si no hay registros, el próximo código será 1
            return 1

    def save(self, *args, **kwargs):
        # Método para guardar el objeto Materi en la base de datos
        if not self.code:
            # Verificamos si el campo code ya tiene un valor asignado
            # Si no tiene un valor (es decir, es None o no está definido), asignamos el próximo código disponible
            self.code = self.get_next_code()
        # Llamamos al método save de la clase padre para guardar el objeto en la base de datos
        super().save(*args, **kwargs)