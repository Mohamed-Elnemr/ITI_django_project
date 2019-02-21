from django.shortcuts import render

# Create your views here.
import json

from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from reservation.models import Hotel
from post.models import Article,Comment
from post.views import get_all_articles,get_comments


# Create your views here.


def index(request):
    top6 = Country.objects.order_by('country_rank')[:6]
    city_list = City.objects.all()[:6]
    country_list=Country.objects.all()
    continent_list=Continents.objects.all()
    articles=get_all_articles(request)[:1]
    context = {'top6': top6,'top_cities': city_list,'country_list':country_list,'continents':continent_list,'articles':articles}
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
        result_count = City.objects.select_related('country').filter(city_name__icontains=query).count()
    else:
        results = City.objects.select_related('country').all()
        result_count  = City.objects.select_related('country').all().count()

    paginator = Paginator(results, 1)
    r = paginator.page(page);
    context = {'search_results': r,'result_count':result_count}

    return render(request, 'website_templates/search_results.html', context)


def get_city(request,city_id):
    city = City.objects.select_related('country').get(city_id=eval(city_id))
    sites = Site.objects.filter(city=eval(city_id)).order_by('site_rank').reverse()

    articles = Article.objects.select_related('user').filter(city=eval(city_id)).order_by('article_rank').reverse()

    top_hotels = Hotel.objects.filter(city=eval(city_id)).order_by('hotel_rank').reverse()[:6]

    comment=get_comments(request,articles)[:1]

    context = {'city': city,'sites':sites,'top_hotels':top_hotels,'articles':articles,'comments':comment}
    return render(request, 'website_templates/single_city.html', context)


def get_continent(request,cont_id):

    continant = Continents.objects.get(cont_id=eval(cont_id))

    top6_countries = Country.objects.filter(cont=eval(cont_id)).order_by('country_rank').reverse()[:6]

    context = {'continant': continant, 'top6_countries': top6_countries}
    return render(request, 'website_templates/single_continant.html', context)


def get_country(request,country_id):

    country = Country.objects.get(country_id=eval(country_id))
    top6_cities = City.objects.filter(country=eval(country_id)).order_by('city_rank').reverse()[:6]

    context = {'country': country, 'top6_cities': top6_cities}
    return render(request, 'website_templates/single_country.html', context)

