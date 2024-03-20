# Generated by Django 5.0.3 on 2024-03-20 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0002_alter_materi_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Careers',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False, verbose_name='codigo')),
                ('name', models.CharField(max_length=150, verbose_name='nombre')),
                ('duration', models.PositiveIntegerField(verbose_name='Duracion en la carrera')),
            ],
        ),
    ]