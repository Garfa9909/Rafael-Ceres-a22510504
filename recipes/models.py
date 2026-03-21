from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length = 100)
    ingredients = models.ManyToManyField(Ingredient, related_name = "recipes")
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length = 100)
    favorites = models.ManyToManyField(Recipe, related_name = "users")
    def __str__(self):
        return self.name


    

