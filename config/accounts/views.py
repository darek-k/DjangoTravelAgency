from django.urls import reverse_lazy
from django.views.generic import CreateView

from config.accounts.forms import SignUpForm


class SignUpView(CreateView):
    template_name = 'form.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')