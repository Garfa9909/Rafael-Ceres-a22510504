from django.contrib import admin
from .models import Degree
from .models import Professor
from .models import Subject
from .models import Technology
from .models import Competence
from .models import Project
from .models import Tfc
from .models import Education
from .models import MakingOf
from .models import Language

class DegreeAdmin(admin.ModelAdmin):
    list_display = ("name", "tipo")
    ordering = ("name", "tipo")
    search_fields = ("name",)

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ("name", "surnames",)
    ordering = ("name", "surnames")
    search_fields = ("name", "surnames")

class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "degree", "year", "ects")
    ordering = ("degree",)
    search_fields = ("name",)

class TechnologyAdmin(admin.ModelAdmin):
    list_display = ("name", "link", "level_of_interest")
    ordering = ("name",)
    search_fields = ("name",)

class CompetenceAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering = ("name",)
    search_fields = ("name",)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "subject")
    ordering = ("name",)
    search_fields = ("name",)

class TfcAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    ordering = ("title",)
    search_fields = ("title",)

class EducationAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering = ("name",)
    search_fields = ("name",)

class MakingOfAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering = ("name",)
    search_fields = ("name",)

class LanguageAdmin(admin.ModelAdmin):
    list_display = ("name", "level")
    ordering = ("level",)
    search_fields = ("name",)

admin.site.register(Degree, DegreeAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Technology, TechnologyAdmin)
admin.site.register(Competence, CompetenceAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Tfc, TfcAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(MakingOf, MakingOfAdmin)
admin.site.register(Language, LanguageAdmin)

