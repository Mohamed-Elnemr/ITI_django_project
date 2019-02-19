from django.shortcuts import render

# Create your views here.
import json

from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from .models import Country,City
from django.core.paginator import Paginator



# Create your views here.


def index(request):
    top6 = Country.objects.order_by('country_rank')[:6]
    city_list = City.objects.all()
    country_list=Country.objects.all()
    context = {'top6': top6,'tag_list': city_list,'country_list':country_list}
    return render(request, 'website_templates/index.html',context)


def top_countries(request):
    top6=Country.objects.order_by('country_rank')[:6]
    context={'top6':top6}
    return render (request,'website_templates/index.html',context)


# def increase_country_rank(request,country_id):
#     Country.objects.filter(pk=country_id).update(country_rank=+1)


def display_cities(request):
    city_list = City.objects.all()
    context = {'tag_list': city_list}
    return render(request, '', context)


# def add_city_reviews(request,city_id,content):
#     City.objects.filter(pk=city_id)

# def autocompleteModel(request):
#     if request.is_ajax():
#         q = request.GET.get('term', '').capitalize()
#         search_qs = City.objects.filter(city_name=q)
#         results = []
#
#         for r in search_qs:
#             db = []
#             db['label'] = r.city_name
#             db['value'] = r.city_name
#             # results.append(r.city_name)
#             results.append(db)
#         data = json.dumps(results)
#     else:
#         data = 'fail'
#     mimetype = 'application/json'
#     return HttpResponse(data, mimetype)


def autocompleteModel(request):

        q = request.GET.get("term", '').capitalize()
        results_ar =[]

        if q:
            results = City.objects.filter(city_name__icontains=q)
        else:
            results = City.objects.all()

        for r in results:
            user_json = {}
            user_json['id'] = r.city_id
            user_json['label'] = r.city_name
            user_json['value'] = r.city_name
            results_ar.append(user_json)

        data = json.dumps(results_ar)
        mimetype = 'application/json'
        return HttpResponse(data, mimetype)




def search(request):
    query = request.GET.get('city')
    page = int(request.GET.get('page', '1'))
    if query:
        results = City.objects.select_related('country').filter(city_name__icontains=query)
    else:
        results = City.objects.select_related('country').all()

    paginator = Paginator(results, 1)
    r = paginator.page(page);
    context = {'search_results': r}

    return render(request, 'website_templates/search_results.html', context)


def get_city(request,city_id):
    city = City.objects.select_related('country').get(city_id=eval(city_id))
    context = {'city': city}
    return render(request, 'website_templates/single_city.html', context)
