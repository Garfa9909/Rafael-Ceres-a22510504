from django.urls import path
from . import views

urlpatterns = [
    path('', views.competences_view, name="index"),
    path('professors/', views.professors_view, name="professors"),
    path('competences/', views.competences_view, name="competences"),
    path('projects/', views.projects_view, name="projects"),
    path('technologies/', views.technologies_view, name="technologies"),
    path('subjects/', views.subjects_view, name="subjects"),
    path('degrees/', views.degrees_view, name="degrees"),
    path('tfcs/', views.tfcs_view, name="tfcs"),
    path('education/', views.education_view, name="education"),
    path('languages/', views.languages_view, name="languages"),
    path('makingof/', views.makingof_view, name="makingof"),

    path("new_project", views.new_project_view, name = "new-project"),
    path("project/<int:id>", views.project_view, name = "project"),
    path("edit_project/<int:id>/", views.edit_project_view, name = "edit-project"),
    path("delete_project/<int:id>/", views.delete_project_view, name = "delete-project"),

    path("new_technology/", views.new_technology_view, name = "new-technology"),
    path("technology/<int:id>", views.technology_view, name = "technology"),
    path("edit_technology/<int:id>/", views.edit_technology_view, name = "edit-technology"),
    path("delete_technology/<int:id>/", views.delete_technology_view, name = "delete-technology"),

    path("new_competence/", views.new_competence_view, name = "new-competence"),
    path("competence/<int:id>", views.competence_view, name = "competence"),
    path("edit_competence/<int:id>/", views.edit_competence_view, name = "edit-competence"),
    path("delete_competence/<int:id>/", views.delete_competence_view, name = "delete-competence"),

    path("new_education/", views.new_education_view, name = "new-education"),
    path("education/<int:id>", views.education_details_view, name = "education-details"),
    path("edit_education/<int:id>/", views.edit_education_view, name = "edit-education"),
    path("delete_education/<int:id>/", views.delete_education_view, name = "delete-education"),

    path("about/", views.about_view, name = "about"),


]