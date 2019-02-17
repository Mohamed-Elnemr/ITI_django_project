from django.contrib import admin

# Register your models here.
from .models import *


class Country_inline(admin.StackedInline):
    model = Country
    extra = 1



class Continents_edit(admin.ModelAdmin):
    list_display = ('cont_name', 'image_tag')
    fieldsets = (
        ['Continents info', {'fields':['cont_image','cont_name']}],
    )

    search_fields = ('cont_name',)

    # inlines = [Country_inline]

class Country_edit(admin.ModelAdmin):
    list_display = ('country_name','cont','image_tag')
    list_display_links = ('country_name','cont')
    # list_editable = ('cont',)
    list_filter = ('cont',)
    fieldsets = (
        ['Country info', {'fields':['country_image','country_name','country_rank','cont']}],
    )
    search_fields = ('country_name','cont__cont_name')



    # def combine_country_cont(self,obj):
    #     return "{} - {}".format(obj.country_name,obj.cont)



class City_edit(admin.ModelAdmin):
    list_display = ('city_name','country','image_tag')
    list_display_links = ('city_name','country')
    # list_editable = ('country',)
    # list_filter = ('country',)
    fieldsets = (
        ['City info', {'fields':['city_image','city_name','city_rank','city_des','city_long','city_lat','country']}],
    )
    search_fields = ('city_name','country__country_name')


class Site_edit(admin.ModelAdmin):
    list_display = ('site_name', 'city','image_tag')
    list_display_links = ('site_name','city')
    # list_editable = ('city',)
    # list_filter = ('country',)
    fieldsets = (
        ['Site info', {'fields':['site_image','site_name','site_des','site_rank','site_review','city']}],
    )
    search_fields = ('site_name','city__city_name')





# register the models
admin.site.register(Continents,Continents_edit)
admin.site.register(Country,Country_edit)
admin.site.register(City,City_edit)
admin.site.register(Site,Site_edit)