from django.db import models
from website.models import City,Country

# Create your models here.

class Hotel(models.Model):
    # fields definition
    def __str__(self):
        return self.hotel_name

    hotel_id = models.AutoField(primary_key=True)
    hotel_name = models.CharField(max_length = 200 ,null=False)
    hotel_des = models.TextField(null=True, blank=True,verbose_name='hotel description')
    hotel_rank = models.IntegerField()
    hotel_review = models.TextField(null=True, blank=True)
    city = models.ForeignKey(City)

class Car(models.Model):
    # fields definition
    def __str__(self):
        return self.car_number

    car_id = models.AutoField(primary_key=True)
    car_type = models.CharField(max_length = 200 ,null=False)
    car_price = models.FloatField(null=False)
    car_number = models.IntegerField(null=False)
    country = models.ForeignKey(Country)

class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_price = models.FloatField(null=False)
    num_of_beds = models.IntegerField(null=False)
    hotel = models.ForeignKey(Hotel)

class Location(models.Model):
    # fields definition
    def __str__(self):
        return self.location_name

    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=200, null=False)
    country = models.ForeignKey(Country)

class CarStatus(models.Model):
    is_available = models.BooleanField(default=True)
    date_from = models.DateField(null=False)
    date_to = models.DateField(null=False)
    loc_from = models.ForeignKey(Location,related_name='location from+')
    loc_to = models.ForeignKey(Location,related_name='location to+')
    car = models.ForeignKey(Car)
