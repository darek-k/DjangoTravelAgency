from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from core.models import Continent, Country, City, Hotel, Airport, Trip

from accounts.forms import SignUpForm


class SignUpView(CreateView):
    template_name = 'form.html'
    form_class = SignUpForm
    success_url = reverse_lazy('trip_list')
