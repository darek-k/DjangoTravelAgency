from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
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


class SignInView(LoginView):
    form_class = AuthenticationForm
    template_name = 'sign_in_form.html'
    success_url = 'trip_list'


class UserLogoutView(LogoutView):
    success_url = 'trip_list'
