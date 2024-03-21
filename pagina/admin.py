from django.contrib import admin
from .models import Materi, Careers, students, Teacher

# Register your models here.
class MateriAdmin(admin.ModelAdmin):
    readonly_fields=('Creation_date', 'update_date')
admin.site.register(Materi, MateriAdmin)
admin.site.register(Careers)
admin.site.register(students)
admin.site.register(Teacher)