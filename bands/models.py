from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class Band(models.Model):
    name = models.CharField(max_length = 100)
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE, related_name = "bands")
    def __str__(self):
        return self.name

class Festival(models.Model):
    name = models.CharField(max_length = 100)
    bands = models.ManyToManyField(Band, related_name = "festivals")
    def __str__(self):
        return self.name
