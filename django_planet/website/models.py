from django.db import models

# Create your models here.

class Continents(models.Model):
    cont_id = models.PositiveIntegerField(primary_key=True)
    cont_name = models.CharField(max_length = 200 ,null=False)

class Country(models.Model):
    country_id = models.PositiveIntegerField(primary_key=True)
    country_name = models.CharField(max_length = 200 , null=False)
    country_rank = models.IntegerField()
    cont_id = models.ForeignKey(Continents)


class City(models.Model):
    city_id = models.PositiveIntegerField(primary_key=True)
    city_name = models.CharField(max_length = 200 , null=False)
    city_rank = models.IntegerField()
    city_des = models.CharField(max_length=250)
    country_id = models.ForeignKey(Country)



class Site(models.Model):
    site_id = models.PositiveIntegerField(primary_key=True)
    site_name = models.CharField(max_length = 200 , null=False)
    site_des = models.CharField(max_length=250)
    site_rank = models.IntegerField()
    site_review = models.CharField(max_length=250)
    city_id = models.ForeignKey(City)

