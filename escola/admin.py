from django.contrib import admin

from .models import Student
from .models import Turn
from .models import Professor

admin.site.register(Student)
admin.site.register(Turn)
admin.site.register(Professor)
