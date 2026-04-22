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
    path("new_project/", views.new_project_view, name = "new-project"),
    path("project/<int:id>", views.project_view, name = "project"),
    path("edit_project/<int:id>/", views.edit_project_view, name = "edit-project"),
    path("delete_project/<int:id>/", views.delete_project_view, name = "delete-project"),


]