"""pro1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from website import views
from django.conf.urls import  url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [

    url(r'^$', views.search),
    url(r'^/city/(?P<city_id>[0-9]+)/$', views.get_city),
    url(r'^/continent/(?P<cont_id>[0-9]+)/$', views.get_continent),
    url(r'^/country/(?P<country_id>[0-9]+)/$', views.get_country),

    # url(r'^/about/$', views.get_country,name="country"),

    # url(r'^search(?[0-9]+)', views.search),


]



