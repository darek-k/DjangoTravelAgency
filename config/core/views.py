import datetime

from core.models import Trip, Country
from django.shortcuts import render
from django.utils.timezone import now
from django.views.generic import ListView, DetailView


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


class TripListView(ListView):
    model = Trip
    template_name = 'core/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TripListView, self).get_context_data(**kwargs)
        context['all_trips'] = Trip.objects.all()
        context['promoted_trips'] = Trip.objects.filter(promoted=True)
        context['last_minute_trips'] = Trip.objects.filter(departure_date__lt=now() + datetime.timedelta(30))
        context['all_countries'] = Country.objects.exclude(name='Polska')
        return context
