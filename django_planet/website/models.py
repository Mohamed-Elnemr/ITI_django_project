from django.db import models

# Create your models here.

class Continents(models.Model):
    # fields definition
    def __str__(self):
        return self.cont_name
    cont_id = models.AutoField(primary_key=True)
    cont_name = models.CharField(max_length = 200 ,null=False,verbose_name='Continent Name')
    cont_image = models.ImageField(upload_to='conts_images',blank=True,verbose_name='Continent Image')

class Country(models.Model):

    def image_tag(self):
        return u'<img src="/media/%s" / style= "width: 50px;height: 50px;">' % self.country_image
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    # fields definition
    def __str__(self):
        return self.country_name

    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length = 200 , null=False)
    country_rank = models.IntegerField()
    country_image = models.ImageField(upload_to='countries_images',blank=True)
    cont = models.ForeignKey(Continents,verbose_name='Continent Name')


class City(models.Model):
    # fields definition
    def __str__(self):
        return self.city_name

    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length = 200 , null=False)
    city_rank = models.IntegerField()
    city_des = models.TextField(null=True, blank=True,verbose_name='City Description')
    city_long = models.FloatField(null=False,verbose_name='City Longitude')
    city_lat = models.FloatField(null=False,verbose_name='City Latitude')
    city_image = models.ImageField(upload_to='cities_images',blank=True)
    country = models.ForeignKey(Country,verbose_name='Country')



class Site(models.Model):

    # fields definition
    def __str__(self):
        return self.site_name

    site_id = models.AutoField(primary_key=True)
    site_name = models.CharField(max_length = 200 , null=False)
    site_des = models.TextField(null=True, blank=True,verbose_name='site description')
    site_rank = models.IntegerField()
    site_review = models.CharField(max_length=250)
    site_image = models.ImageField(upload_to='sities_images',blank=True)
    city = models.ForeignKey(City)

