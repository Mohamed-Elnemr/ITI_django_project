from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from user.forms import *

# Create your views here.
def index(request):
    return render(request, "../templates/user_templates/index.html")

def getCarHistory(request):
    return render(request, "../templates/user_templates/car_history.html")

def getHotelHistory(request):
    return render(request, "../templates/user_templates/hotel_history.html")


def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/")


	else:
		form = RegistrationForm()
		context = {'edit_form': form}
		return render(request, '../templates/user_templates/registration.html', context)



def editProfile(request, username):
	user = User.objects.get(username = username)
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance= user)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/")


	else:
		form = EditProfileForm(instance = user)
		context = {'edit_form': form}
		return render(request, "../templates/user_templates/edit_profile.html",context)

