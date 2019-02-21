from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from user.forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import *
# Create your views here.
def index(request):

    return render(request, "../templates/user_templates/index.html")

def getCarHistory(request):
	allCarHistory = CarHistory.objects.select_related('car').filter(user_id=request.user.id)
	context = {'allHistory': allCarHistory}
	return render(request, "user_templates/car_history.html",context)

def getHotelHistory(request):
	allHotelHistory = HotelHistory.objects.select_related('hotel').filter(user_id=request.user.id)
	context = {'allHistory' : allHotelHistory}
	return render(request, "user_templates/hotel_history.html", context)


def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return HttpResponseRedirect("/")
		else:
			return HttpResponseRedirect("/user/registration/")
	else:
		form = RegistrationForm()
		context = {'registration_form': form}
		return render(request, 'user_templates/registration.html', context)



def editProfile(request):
	# user = User.objects.get(username = username)
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance= request.user)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/")


	else:
		form = EditProfileForm(instance = request.user)
		context = {'edit_form': form}
		return render(request, "../templates/user_templates/edit_profile.html",context)

