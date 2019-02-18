from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from user.form import RegistrationForm

# Create your views here.
def index(request):
    return render(request, "../templates/user_templates/index.html")

def getCarHistory(request):
    return render(request, "../templates/user_templates/car_history.html")

def getHotelHistory(request):
    return render(request, "../templates/user_templates/hotel_history.html")


def editProfile(request):
    return render(request, "../templates/user_templates/edit_profile.html")


def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/")


	else:
		form = RegistrationForm()
		context = {'register_form': form}
		return render(request, '../templates/user_templates/registration.html', context)

