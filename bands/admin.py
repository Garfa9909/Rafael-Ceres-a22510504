from django.contrib import admin

from .models import Genre
from .models import Band
from .models import Festival

admin.site.register(Genre)
admin.site.register(Band)
admin.site.register(Festival)
