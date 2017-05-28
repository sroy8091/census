from django.db import models

# Create your models here.


class MainVisual(models.Model):
    year = models.IntegerField()
    totalpop = models.IntegerField()
    male = models.IntegerField()
    female = models.IntegerField()

