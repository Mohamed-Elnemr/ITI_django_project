from django.shortcuts import render

from user.models import HotelHistory, CarHistory
from website.models import City
from .models import Location, Hotel, Car, CarStatus
from django.http import HttpResponseRedirect
from .forms import HotelReservationForm, CarReservationForm
from django.contrib.auth.models import User

# Create your views here.
def reserve_hotel(request):
    # all_cities = City.objects.all()
    # all_hotels = Hotel.objects.all()
    hotel_form = HotelReservationForm()
    hotel_form.fields['hotel'].queryset = Hotel.objects.filter(city_id=1)
    if request.method == 'POST':
        form = HotelReservationForm(request.POST)
        if form.is_valid():
            user = request.user
            hotel_instance = HotelHistory.objects.create(user_id = user.id, hotel=form.cleaned_data.get('hotel'), date_from = form.cleaned_data.get('date_from'),
                                          date_to = form.cleaned_data.get('date_to'), num_of_person = form.cleaned_data.get('num_of_person'))
            # form.save()
            hotel_instance.save()
            return HttpResponseRedirect("/")
    else:
        hotel_form = HotelReservationForm()
        context = {'hotel_reservation_form': hotel_form}
        return render(request, 'reservation_templates/hotel_reserve.html', context)



def reserve_car(request):
    # all_cities = City.objects.all()
    # all_hotels = Hotel.objects.all()
    car_form = CarReservationForm()
    car_form.fields['car'].queryset = Car.objects.filter(country_id=1)
    # availability = CarStatus.objects.update(is_available="False")
    # availability.save()
    if request.method == 'POST':
        form = CarReservationForm(request.POST)
        if form.is_valid():
            user = request.user
            car_instance = CarHistory.objects.create(user_id=user.id,
                                                     car=form.cleaned_data.get('car'),
                                                     country=form.cleaned_data.get('country_id'),
                                                     date_from=form.cleaned_data.get('date_from'),
                                                     date_to=form.cleaned_data.get('date_to'),
                                                     loc_from=form.cleaned_data.get('loc_from'),
                                                     loc_to=form.cleaned_data.get('loc_to'))
            # form.save()
            car_instance.save()
            return HttpResponseRedirect("/")
    else:
        car_form = CarReservationForm()
        context = {'car_reservation_form': car_form}
        return render(request, 'reservation_templates/car_reserve.html', context)

    # all_cities = City.objects.all()
    # requested_car_id = Car.objects.all()
    # availability = Car.objects.update(is_available="False")
    # availability.save()
    # all_locations = Location.objects.all()
    # context = {'allCities': all_cities, 'allCars': requested_car_id, 'allLocations': all_locations}
    # return render('reservation_templates/car_reserve.html', context)


def get_all_hotels(request, requested_id):
    all_hotels = Hotel.objects.filter(city=requested_id)
    context = {'allHotels': all_hotels}
    return render(request, '', context)


def get_all_cars(request):
    available_cars = CarStatus.objects.filter(is_available="True")
    context = {'allCars': available_cars}
    return render(request, '', context)


def add_hotel(request):
    h = Hotel.objects.create()
    return render(request, '', h)


def add_car(request):
    c = Car.objects.create()
    return render(request, '', c)

