from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from core.models import Continent, Country, City, Hotel, Airport, Trip

from accounts.forms import SignUpForm


class AdminListView(ListView):
    model = Trip
    template_name = 'accounts/admin_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AdminListView, self).get_context_data(**kwargs)
        context['continents'] = Continent.objects.all()
        context['countries'] = Country.objects.all()
        context['cities'] = City.objects.all()
        context['hotels'] = Hotel.objects.all()
        context['airports'] = Airport.objects.all()
        context['trips'] = Trip.objects.all()
        return context


class AddDetailView(DetailView):
    model = Trip
    template_name = 'accounts/admin_list.html'


class SignUpView(CreateView):
    template_name = 'form.html'
    form_class = SignUpForm
    success_url = reverse_lazy('trip_list')
