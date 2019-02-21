from django.contrib import admin
from .models import *
# Register your models here.


class hotel_edit(admin.ModelAdmin):
    list_display = ('hotel_name','city','image_tag')
    list_display_links = ('hotel_name','city')

    list_filter = ('city',)
    fieldsets = (
        ['hotel info', {'fields':['hotel_image','hotel_name','hotel_rank','city']}],
    )
    search_fields = ('hotel_name','city__city_name')


class car_edit(admin.ModelAdmin):
    list_display = ('car_number','car_type','car_price','country','image_tag')
    list_display_links = ('car_number','country')

    # list_filter = ('city',)
    fieldsets = (
        ['car info', {'fields':['car_image','car_number','car_type','car_price','country']}],
    )
    search_fields = ('car_number','car_type','country__country_name')



admin.site.register(Hotel,hotel_edit)
admin.site.register(Car,car_edit)