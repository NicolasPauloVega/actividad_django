# Generated by Django 5.0.3 on 2024-03-20 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0003_careers'),
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False, verbose_name='codigo')),
                ('name', models.CharField(max_length=150, verbose_name='nombre')),
                ('last_name', models.CharField(max_length=150, verbose_name='apellido')),
                ('email', models.EmailField(max_length=254, verbose_name='correo')),
                ('phone', models.CharField(max_length=20, verbose_name='phone')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('update_date', models.DateField(auto_now=True, verbose_name='fecha de actualizacion')),
            ],
            options={
                'verbose_name': 'Estudiantes',
            },
        ),
        migrations.AlterModelOptions(
            name='careers',
            options={'verbose_name': 'Carreras'},
        ),
    ]
