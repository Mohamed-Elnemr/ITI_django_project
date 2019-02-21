from django import forms
from user.models import HotelHistory, CarHistory


class HotelReservationForm(forms.ModelForm):
    class Meta:
        model = HotelHistory
        fields = ('hotel', 'date_from', 'date_to', 'num_of_person')


class CarReservationForm(forms.ModelForm):
    class Meta:
        model = CarHistory
        fields = ('car', 'date_from', 'date_to', 'loc_from', 'loc_to')

