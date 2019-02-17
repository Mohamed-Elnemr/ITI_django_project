from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "../templates/user_templates/index.html")

def getCarHistory(request):
    return render(request, "../templates/user_templates/car_history.html")

def getHotelHistory(request):
    return render(request, "../templates/user_templates/hotel_history.html")


def editProfile(request):
    return render(request, "../templates/user_templates/edit_profile.html")
