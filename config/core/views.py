import datetime

from core.forms import ContinentForm, CountryForm, CityForm, HotelForm, AirportForm, TripForm
from core.models import Trip, Country
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views.generic import ListView, DetailView, CreateView


def template_elements(request):
    """ Do usunięcia po zrobieniu frontendu"""
    return render(request, 'core/elements.html')


def hotels(request):
    """ Do usunięcia po zrobieniu frontendu"""
    return render(request, 'core/hotels.html')


def about(request):
    return render(request, 'core/about.html')


def blog_home(request):
    return render(request, 'core/blog-home.html')


def blog_single(request):
    return render(request, 'core/blog-single.html')


def contact(request):
    return render(request, 'core/contact.html')


def insurance(request):
    return render(request, 'core/insurance.html')


def packages(request):
    return render(request, 'core/packages.html')


class TripDetailsView(DetailView):
    model = Trip
    template_name = 'core/trip_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['duration'] = Trip.departure_date
        return context


class TripListView(ListView):
    model = Trip
    template_name = 'core/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TripListView, self).get_context_data(**kwargs)
        context['all_trips'] = Trip.objects.all()
        context['promoted_trips'] = Trip.objects.filter(promoted=True)[:3]
        context['last_minute_trips'] = Trip.objects.filter(departure_date__lt=now() + datetime.timedelta(30))[:3]
        context['all_countries'] = Country.objects.exclude(name='Polska')
        return context


class ContinentCreateView(CreateView):
    title = 'Add continent'
    template_name = 'form.html'
    form_class = ContinentForm
    success_url = reverse_lazy('core:add_continent')

    def post(self, request, *args, **kwargs):
        result = super().post(request, *args, **kwargs)
        return result


class CountryCreateView(CreateView):
    title = 'Add country'
    template_name = 'form.html'
    form_class = CountryForm
    success_url = reverse_lazy('core:add_country')


class CityCreateView(CreateView):
    title = 'Add city'
    template_name = 'form.html'
    form_class = CityForm
    success_url = reverse_lazy('core:add_city')


class HotelCreateView(CreateView):
    title = 'Add hotel'
    template_name = 'form.html'
    form_class = HotelForm
    success_url = reverse_lazy('core:add_hotel')


class AirportCreateView(CreateView):
    title = 'Add airport'
    template_name = 'form.html'
    form_class = AirportForm
    success_url = reverse_lazy('core:add_airport')


class TripCreateView(CreateView):
    title = 'Add trip'
    template_name = 'form.html'
    form_class = TripForm
    success_url = reverse_lazy('core:add_trip')
