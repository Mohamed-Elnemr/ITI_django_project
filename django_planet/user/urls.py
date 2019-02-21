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

from user import views
from django.conf.urls import  url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
url(r'^$', views.index),
    url(r'^car_history/', views.getCarHistory),
    url(r'^hotel_history/(?P<hotel_id>[0-9]+)/$', views.getHotelHistory),
    url(r'^edit/(?P<username>[a-zA-Z]+)$', views.editProfile),
    url(r'^registration/', views.register)

]


