from django.db import models



class Degree(models.Model):
    TYPES = [('L', 'Bachelor'), ('M', 'Master')] #Each course is bachelor's or master's degree
    name = models.CharField(max_length = 100)
    tipo = models.CharField(choices = TYPES, null = True)
    description = models.CharField(max_length = 1000, null = True)

    def __str__(self):
        return self.name

class Professor(models.Model):
    name = models.CharField(max_length = 100)
    surnames = models.CharField(max_length = 100)
    mail = models.CharField(max_length = 50)
    page_link = models.URLField(max_length = 100)

    def __str__(self):
        return f"{self.name} {self.surnames}"

class Subject(models.Model):
    YEARS = [(1, "First"), (2, "Second"), (3, "Third")]
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)
    program = models.CharField(max_length = 1000)
    ects = models.IntegerField()
    code = models.CharField(max_length=20, unique = True)
    year = models.IntegerField(choices = YEARS)
    image = models.ImageField(upload_to="portfolio/fotos")
    professors = models.ManyToManyField(Professor, related_name = "subjects")
    degree = models.ForeignKey(Degree, on_delete = models.CASCADE, related_name = "subjects")

    def __str__(self):
        return self.name

class Competence(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Technology(models.Model):
    INTEREST = [(1, "Very low"), (2, "Low"), (3, "Medium"), (4, "High"), (5, "Very high")]
    name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to="portfolio/fotos")
    link = models.URLField(max_length = 100)
    description = models.CharField(max_length = 1000)
    level_of_interest = models.IntegerField(choices = INTEREST)
    competences = models.ManyToManyField(Competence, related_name = "technologies")

    def __str__(self):
        return self.name



class Project(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)
    competences = models.ManyToManyField(Competence, related_name = "projects")
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE, related_name = "projects")

    def __str__(self):
        return self.name

class Tfc(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    year = models.IntegerField()
    description = models.CharField(max_length = 1000)
    degree = models.ForeignKey(Degree, on_delete = models.CASCADE, related_name = "tfcs")

    def __str__(self):
        return self.title

class Education(models.Model):
    name = models.CharField(max_length = 100)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    def __str__(self):
        return self.name

class MakingOf(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)
    picture = models.ImageField(upload_to = "making_of")

class Language(models.Model):   #New entity introduced by me, in order to list the language the person knows and level of dominance
    LEVELS = [(7, "Native"), (1, "A1"), (2, "A2"), (3, "B1"), (4, "B2"), (5, "C1"), (6, "C2")]
    name = models.CharField(max_length=30)
    level = models.IntegerField(choices = LEVELS)





