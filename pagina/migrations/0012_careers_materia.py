# Generated by Django 5.0.3 on 2024-04-06 20:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0011_alter_teacher_materi'),
    ]

    operations = [
        migrations.AddField(
            model_name='careers',
            name='materia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pagina.materi', verbose_name='materia'),
        ),
    ]
