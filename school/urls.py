from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.courses_view, name="courses"),
    path('professors/', views.professors_view, name="professors"),
    path('students/', views.students_view, name="students"),
    path('', views.courses_view),
    path('course/<int:id>', views.course_view, name="course"),
]