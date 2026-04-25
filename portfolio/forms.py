from django import forms
from .models import Project, Technology, Competence, Education


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"


class TechnologyForm(forms.ModelForm):
    class Meta:
        model = Technology
        fields = "__all__"

class CompetenceForm(forms.ModelForm):
    class Meta:
        model = Competence
        fields = "__all__"

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = "__all__"
