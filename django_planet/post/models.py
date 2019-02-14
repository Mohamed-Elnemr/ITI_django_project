from django.db import models

# Create your models here.


class Articles(models.Model):
    number=models.IntegerField()

class Comments(models.Model):
    number = models.IntegerField()


