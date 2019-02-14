from django.db import models

# Create your models here.


class Countries(models.Model):
    name = models.CharField(max_length=20)
    rank = models.IntegerField(max_length=12)


class Cities(models.Model):
    name = models.CharField(max_length=20)

class Sites(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    rating = models.IntegerField(max_length=20)
    reviews = models.TextField()
#

