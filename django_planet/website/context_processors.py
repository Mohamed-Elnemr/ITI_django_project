

from .models import Continents


def Continents_processor(request):

 continent_list = Continents.objects.all()

 return {'continent_list': continent_list}

