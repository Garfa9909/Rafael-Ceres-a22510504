from django.shortcuts import render, redirect

from .models import Professor, Subject, Degree, Project, Technology, Competence, Tfc, Education, Language, MakingOf
from .forms import ProjectForm, TechnologyForm, CompetenceForm, EducationForm
from django.contrib.auth.decorators import user_passes_test, login_required

def es_gestor(user):
    return user.groups.filter(name='gestor-portfolio').exists()

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
    return render(request, 'portfolio/projects.html', {'projects': projects, 'es_gestor':es_gestor(request.user)})


def competences_view(request):
    competences = Competence.objects.prefetch_related('technologies').all()
    return render(request, 'portfolio/competences.html', {'competences': competences, 'es_gestor':es_gestor(request.user)})


def technologies_view(request):
    technologies = Technology.objects.prefetch_related('competences').all()
    return render(request, 'portfolio/technologies.html', {'technologies': technologies, 'es_gestor':es_gestor(request.user)})

def tfcs_view(request):
    tfcs = Tfc.objects.select_related('degree').all()
    return render(request, 'portfolio/tfcs.html', {'tfcs': tfcs})

def education_view(request):
    education = Education.objects.all().order_by('start_year')
    return render(request, 'portfolio/education.html', {'education': education, 'es_gestor':es_gestor(request.user)})

def languages_view(request):
    languages = Language.objects.all()
    return render(request, 'portfolio/languages.html', {'languages': languages})

def makingof_view(request):
    makingof = MakingOf.objects.all()
    return render(request, 'portfolio/makingof.html', {'makingof': makingof})


@login_required
def project_view(request, id):
    project = Project.objects.get(id=id)
    context = {'project':project, 'es_gestor':es_gestor(request.user)}

    return render(request, 'portfolio/project.html', context)

@login_required
@user_passes_test(es_gestor)
def new_project_view(request):
    form = ProjectForm(request.POST, request.FILES)

    if(form.is_valid()):
        form.save()
        return redirect('projects')
    
    context = {'form':form}
    return render(request, "portfolio/new_project.html", context)


@login_required
@user_passes_test(es_gestor)
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
@login_required
@user_passes_test(es_gestor)
def delete_project_view(request, id):

    Project.objects.get(id=id).delete()
    return redirect("projects")




@login_required
def technology_view(request, id):
    technology = Technology.objects.get(id=id)
    context = {'technology':technology, 'es_gestor':es_gestor(request.user)}

    return render(request, 'portfolio/technology.html', context)

@login_required
@user_passes_test(es_gestor)
def new_technology_view(request):
    form = TechnologyForm(request.POST or None, request.FILES)

    if(form.is_valid()):
        form.save()
        return redirect('technologies')

    context = {'form':form}
    return render(request, 'portfolio/new_technology.html', context)

@login_required
@user_passes_test(es_gestor)
def edit_technology_view(request, id):

    technology = Technology.objects.get(id=id)
    
    if(request.POST):
        form = TechnologyForm(request.POST or None, request.FILES, instance = technology)
        if(form.is_valid()):
            form.save()
            return redirect('technologies')
    else:
        form = TechnologyForm(instance=technology)

    context = {'form':form, 'technology':technology}
    return render(request, "portfolio/edit_technology.html", context)

@login_required
@user_passes_test(es_gestor)
def delete_technology_view(request, id):

    Technology.objects.get(id=id).delete()
    return redirect("technologies")



@login_required
def competence_view(request, id):
    competence = Competence.objects.get(id=id)
    context = {'competence':competence, 'es_gestor':es_gestor(request.user)}

    return render(request, 'portfolio/competence.html', context)

@login_required
@user_passes_test(es_gestor)
def new_competence_view(request):
    form = CompetenceForm(request.POST or None, request.FILES)

    if(form.is_valid()):
        form.save()
        return redirect('competences')

    context = {'form':form}
    return render(request, 'portfolio/new_competence.html', context)

@login_required
@user_passes_test(es_gestor)
def edit_competence_view(request, id):

    competence = Competence.objects.get(id=id)
    
    if(request.POST):
        form = CompetenceForm(request.POST or None, request.FILES, instance = competence)
        if(form.is_valid()):
            form.save()
            return redirect('competences')
    else:
        form = CompetenceForm(instance=competence)

    context = {'form':form, 'competence':competence}
    return render(request, "portfolio/edit_competence.html", context)

@login_required
@user_passes_test(es_gestor)
def delete_competence_view(request, id):

    Competence.objects.get(id=id).delete()
    return redirect("competences")






@login_required
def education_details_view(request, id):
    education = Education.objects.get(id=id)
    context = {'education':education, 'es_gestor':es_gestor(request.user)}

    return render(request, 'portfolio/education_details.html', context)

@login_required
@user_passes_test(es_gestor)
def new_education_view(request):
    form = EducationForm(request.POST or None, request.FILES)

    if(form.is_valid()):
        form.save()
        return redirect('education')

    context = {'form':form}
    return render(request, 'portfolio/new_education.html', context)

@login_required
@user_passes_test(es_gestor)
def edit_education_view(request, id):

    education = Education.objects.get(id=id)
    
    if(request.POST):
        form = EducationForm(request.POST or None, request.FILES, instance = education)
        if(form.is_valid()):
            form.save()
            return redirect('education')
    else:
        form = EducationForm(instance=education)

    context = {'form':form, 'education':education}
    return render(request, "portfolio/edit_education.html", context)

@login_required
@user_passes_test(es_gestor)
def delete_education_view(request, id):

    Education.objects.get(id=id).delete()
    return redirect("education")

@login_required
def about_view(request):
    makingof = MakingOf.objects.all()
    mvt_entry = MakingOf.objects.get(name = "MVT Model")
    er_entry = MakingOf.objects.get(name = "ER diagram")
    technologies = Project.objects.get(name = "Portfolio").technologies.all()
    map_entry = MakingOf.objects.get(name = "Application map")
    return render(request, 'portfolio/about.html', {'makingof': makingof, 'mvt':mvt_entry, 'er':er_entry, 'technologies':technologies, 'map':map_entry})