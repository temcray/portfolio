from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Position(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Experience(models.Model):
    school = models.CharField(max_length=50)
    description = models.TextField()
    year = models.IntegerField()
    position = models.ManyToManyField("Position")

    def __str__(self):
        return f"{self.school} ({self.year})"
    