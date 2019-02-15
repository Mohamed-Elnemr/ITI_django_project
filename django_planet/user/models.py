from django.db import models
from reservation.models import Hotel,Car,Location
from website.models import Country

# Create your models here.

class HotelHistory(models.Model):
    user_id =  models.PositiveIntegerField(default=1)
    hotel_id = models.ForeignKey(Hotel)
    date_from = models.DateField(null=False)
    date_to = models.DateField(null=False)
    num_of_person = models.PositiveIntegerField()

class CarHistory(models.Model):
    user_id =  models.PositiveIntegerField(default=1)
    car_id = models.ForeignKey(Car)
    country_id = models.ForeignKey(Country)
    date_from = models.DateField(null=False)
    date_to = models.DateField(null=False)
    loc_from = models.ForeignKey(Location,related_name='location from+')
    loc_to = models.ForeignKey(Location,related_name='location to+')
