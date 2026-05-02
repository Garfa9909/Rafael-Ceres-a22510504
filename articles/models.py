from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    text = models.TextField()
    picture = models.ImageField(upload_to='articles/')
    link = models.URLField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}: {self.text}"
