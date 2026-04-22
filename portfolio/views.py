from django.shortcuts import render, redirect

from .models import Professor, Subject, Degree, Project, Technology, Competence, Tfc, Education, Language, MakingOf
from .forms import ProjectForm

def professors_view(request):
    professors = Professor.objects.prefetch_related('subjects').all()
    return render(request, 'portfolio/professors.html', {'professors': professors})

def subjects_view(request):
    subjects = Subject.objects.select_related('degree').prefetch_related('professors').all()
    return render(request, 'portfolio/subjects.html', {'subjects': subjects})

def degrees_view(request):
    degrees = Degree.objects.all()
    return render(request, 'portfolio/degrees.html', {'degrees': degrees})

def projects_view(request):
    projects = Project.objects.select_related('subject').all()
    return render(request, 'portfolio/projects.html', {'projects': projects})


def competences_view(request):
    competences = Competence.objects.prefetch_related('technologies').all()
    return render(request, 'portfolio/competences.html', {'competences': competences})

def technologies_view(request):
    technologies = Technology.objects.prefetch_related('competences').all()
    return render(request, 'portfolio/technologies.html', {'technologies': technologies})

def tfcs_view(request):
    tfcs = Tfc.objects.select_related('degree').all()
    return render(request, 'portfolio/tfcs.html', {'tfcs': tfcs})

def education_view(request):
    education = Education.objects.all().order_by('start_year')
    return render(request, 'portfolio/education.html', {'education': education})

def languages_view(request):
    languages = Language.objects.all()
    return render(request, 'portfolio/languages.html', {'languages': languages})

def makingof_view(request):
    makingof = MakingOf.objects.all()
    return render(request, 'portfolio/makingof.html', {'makingof': makingof})



def project_view(request, id):
    project = Project.objects.get(id=id)
    context = {'project':project}

    return render(request, 'portfolio/project.html', context)

def new_project_view(request):
    form = ProjectForm(request.POST or None, request.FILES)

    if(form.is_valid()):
        form.save()
        return redirect('projects')

    context = {'form':form}
    return render(request, 'portfolio/new_project.html', context)

def edit_project_view(request, id):

    project = Project.objects.get(id=id)
    
    if(request.POST):
        form = ProjectForm(request.POST or None, request.FILES, instance = project)
        if(form.is_valid()):
            form.save()
            return redirect('projects')
    else:
        form = ProjectForm(instance=project)

    context = {'form':form, 'project':project}
    return render(request, "portfolio/edit_project.html", context)

def delete_project_view(request, id):

    Project.objects.get(id=id).delete()
    return redirect("projects")