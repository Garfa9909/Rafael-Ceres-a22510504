from django.shortcuts import render
from .models import Course, Professor, Student

def courses_view(request):

    courses = Course.objects.select_related('professor').prefetch_related('students').all()
    return render(request, 'school/courses.html', {'courses': courses})

def professors_view(request):

    professors = Professor.objects.all()
    return render(request, 'school/professors.html', {'professors': professors})

def students_view(request):

    students = Student.objects.all()
    return render(request, 'school/students.html', {'students': students})

def course_view(request, id):
    course=Course.objects.get(id=id)       
    return render(request, 'school/course.html', {'course': course})