from django.db import models

# Create your models here.
class FirstModel(models.Model):
    name = models.CharField(max_length=100)
    age  = models.IntegerField(default=0)
    salary = models.FloatField(default=0)

