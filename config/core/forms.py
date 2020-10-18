from django import forms
from core.models import Continent, Country, City, Trip, Airport, Hotel, TripPurchase
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import Textarea, SelectDateWidget

# from accounts.models import Profile
from django.utils.datetime_safe import datetime


class ContinentForm(forms.ModelForm):
    class Meta:
        model = Continent
        fields = (
            'name',
        )
        labels = {
            'name': ('Nazwa')
        }


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = (
            'name', 'continent', 'country_image',
        )
        labels = {
            'name': ('Nazwa'), 'continent': ('Kontynent')
        }


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = (
            'name', 'country',
        )
        labels = {
            'name': ('Nazwa'), 'country': ('Kraj')
        }


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = (
            'name', 'stars', 'description', 'city', 'location', 'swimming_pool', 'wifi', 'air_condition',
            'room_service', 'restaurant', 'gym',
        )
        labels = {
            'name': ('Nazwa'), 'stars': ('Liczba gwiazdek'), 'description': ('Opis'), 'city': ('Miasto'),
            'location': ('Lokalizacja'), 'swimming_pool': ('Basen'), 'wifi': ('Wifi'),
            'air_condition': ('Klimatyzacja'),
            'room_service': ('Obsługa hotelowa'), 'restaurant': ('Restauracja'), 'gym': ('Siłownia'),
        }
        help_texts = {
            'location': ('Wstaw link z lokalizacją hotelu z GoogleMaps')
        }


class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = (
            'name', 'city'
        )
        labels = {
            'name': ('Nazwa'), 'city': ('Miasto')
        }


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = (
            'departure_city', 'departure_airport', 'arrival_city', 'arrival_hotel', 'arrival_airport',
            'departure_date',
            'arrival_date', 'return_date', 'back_home_date', 'catering_option', 'price_for_adult',
            'price_for_child',
            'promoted',
        )
        labels = {
            'departure_city': ('Miasto wylotu'), 'departure_airport': ('Lotnisko wylotu'),
            'arrival_city': ('Miasto przylotu'), 'arrival_airport': ('Lotnisko przylotu'),
            'departure_date': ('Data wylotu'), 'arrival_date': ('Data przylotu'), 'return_date': ('Data odlotu'),
            'back_home_date': ('Data powrotu'), 'catering_option': ('Wyżywienie'),
            'price_for_adult': ('Cena za os. dorosłą'), 'price_for_child': ('Cena za dziecko'),
            'promoted': ('Promować?')
        }
        help_texts = {
            'promoted': ('Wycieczka będzie wyświetlana na głównej stronie'),
        }


class TripPurchaseForm(forms.ModelForm):
    class Meta:
        model = TripPurchase
        fields = (
            'trip', 'main_booker', 'adults_number', 'kids_number', 'final_price', 'test_char_field'
        )

        labels = {
            'adults_number': ('Liczba osób dorosłych'), 'kids_number': ('Liczba dzieci')
        }

        widgets = {
            'trip': forms.HiddenInput(), 'main_booker': forms.HiddenInput(), 'final_price': forms.HiddenInput(),
            'test_char_field': forms.HiddenInput(),
        }

