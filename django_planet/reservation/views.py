from django.shortcuts import render
from website.models import City
from reservation.models import Location, Hotel, Car, CarStatus
from django.http import HttpResponseRedirect


# Create your views here.
def reserve_hotel(requested_hotel_id):
    all_cities = City.objects.all()
    requested_hotel = Hotel.objects.filter(hotel_id=requested_hotel_id)
    context = {'allCities': all_cities, 'allHotels': requested_hotel}
    return HttpResponseRedirect('../templates/reservation_templates/hotel_reserve.html')


def reserve_car(requested_car_id):
    all_cities = City.objects.all()
    requested_car_id = Car.objects.filter(car_id=requested_car_id)
    availability = Car.objects.update(is_available="False")
    availability.save()
    all_locations = Location.objects.all()
    context = {'allCities': all_cities, 'allCars': requested_car_id, 'allLocations': all_locations}
    return HttpResponseRedirect('../templates/reservation_templates/car_reserve.html')


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

