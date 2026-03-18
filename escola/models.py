from django.db import models

class Turn(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    turn = models.ForeignKey(Turn, on_delete = models.CASCADE, related_name = "students")
    def __str__(self):
        return self.name

class Professor(models.Model):
    name = models.CharField(max_length=100)
    turn = models.OneToOneField(Turn, on_delete = models.CASCADE, related_name = "professor")
