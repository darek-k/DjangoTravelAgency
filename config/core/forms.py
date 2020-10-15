from django import forms
from core.models import Continent, Country, City, Trip, Airport, Hotel, TripPurchase


class ContinentForm(forms.ModelForm):
    class Meta:
        model = Continent
        fields = (
            'name',
        )


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = (
            'name', 'continent',
        )


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = (
            'name', 'country',
        )


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = (
            'name', 'stars', 'description', 'city', 'location', 'swimming_pool', 'wifi', 'air_condition',
            'room_service', 'restaurant', 'gym',
        )


class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = (
            'name', 'city'
        )


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = (
            'departure_city', 'departure_airport', 'arrival_city', 'arrival_hotel', 'arrival_airport', 'departure_date',
            'arrival_date', 'return_date', 'catering_option', 'price_for_adult', 'price_for_child', 'promoted',
        )


class TripPurchaseForm(forms.ModelForm):
    class Meta:
        model = TripPurchase
        fields = (
            'trip', 'main_booker', 'adults_number', 'kids_number', 'final_price',
        )

# class TripSearchForm(forms.Form):
#     search_departure_city = forms.CharField(
#         required=False, label='Skąd', widget=forms.TextInput(attrs={'placeholder': 'search here!'})
#     )
#
#     search_arrival_city = forms.CharField(
#         required=False, label='Dokąd', widget=forms.TextInput(attrs={'placeholder': 'search here!'})
#     )
#
#     search_hotel = forms.CharField(
#         required=False, label='Hotel', widget=forms.TextInput(attrs={'placeholder': 'search here!'})
#     )
#
#     search_price_min = forms.IntegerField(
#         required=False, label='Min price'
#     )
#
#     search_price_max = forms.IntegerField(
#         required=False, label='max price'
#     )
