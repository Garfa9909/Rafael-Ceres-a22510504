from django.contrib import admin

from .models import Course, Professor, Student

admin.site.register(Student)
admin.site.register(Professor)

class CourseAdmin(admin.ModelAdmin):
    filter_horizontal = ('students',)  # permite adicionar mais facilmente alunos ao curso
    
admin.site.register(Course, CourseAdmin)
