from django.db import models

# Create your models here.
class Nono(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=200)
    replace = models.CharField(max_length=200)