from django.shortcuts import render
from website.models import Country

# Create your views here.

def profile(request):
    return render(request, 'user_templates/profile.html')

def test(request,country_id):

    country = Country.objects.select_related('cont').get(country_id=eval(country_id))
    # print(country.cont.cont_id)
    context = {'country': country}

    return render(request, 'user_templates/test.html',context)