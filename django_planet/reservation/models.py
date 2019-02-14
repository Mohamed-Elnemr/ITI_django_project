from django.db import models

# Create your models here.

class Hotels(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    number_of_rooms=models.IntegerField()
    price=models.IntegerField()




class Cars (models.Model):
    type = models.CharField(max_length=100)
    price=models.IntegerField()





class Locations(models.Model):
    pass


