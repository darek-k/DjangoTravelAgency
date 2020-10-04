import datetime

from core.models import Trip, Hotel
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.utils.timezone import now
from django.views.generic import ListView, DetailView


def template_elements(request):
    """ Do usunięcia po zrobieniu frontendu"""
    return render(request, 'core/elements.html')


def hotels(request):
    """ Do usunięcia po zrobieniu frontendu"""
    return render(request, 'core/hotels.html')


class TripDetailsView(DetailView):
    model = Trip
    template_name = 'core/trip_details.html'


class TripListView(ListView):
    model = Trip
    template_name = 'core/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['promoted_trips'] = Trip.objects.filter(promoted=True)
        context['last_minute_trips'] = Trip.objects.filter(departure_date__lt=now() + datetime.timedelta(30))
        return context


# class LastMinuteView(ListView):
#     model = Trip
#     template_name = 'core/index.html'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data()
#         context['last_minute_trips'] = Trip.objects.all()
#         return context
