from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from accounts.forms import UserRegisterForm


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'sign_up_form.html'
    success_url = reverse_lazy('trip_list')
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"

