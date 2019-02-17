from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Country,City



# Create your views here.


def index(request):
    return render(request, 'website/index.html')
#
def top_countries(request):
   return  Country.objects.order_by('country_rank')[:6]


# def increase_country_rank(request,country_id):
#     Country.objects.filter(pk=country_id).update(country_rank=+1)


def display_cities(request):
    city_list = City.objects.all()
    context = {'tag_list': city_list}
    return render(request, '', context)


# def add_city_reviews(request,city_id,content):
#     City.objects.filter(pk=city_id)






