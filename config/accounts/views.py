from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from accounts.forms import SignUpForm


def add_view(request):
    return render(request, 'accounts/add_view.html')


class SignUpView(CreateView):
    template_name = 'form.html'
    form_class = SignUpForm
    success_url = reverse_lazy('trip_list')
