from django.db import models

class Meta:
    unique_together=("pt", "date", "time")

class Client(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class Pt(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class Session(models.Model):
    date = models.DateField()
    time = models.TimeField()
    client = models.ForeignKey(Client, on_delete = models.CASCADE, related_name = "sessions")
    pt = models.ForeignKey(Pt, on_delete = models.CASCADE, related_name = "sessions")
    def __str__(self):
        return f"{self.pt}; {self.date}, {self.time}"
