from core.models import Trip
from django.views.generic import ListView


class PromotedTripsView(ListView):
    model = Trip
    template_name = 'core/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['promoted_trips_list'] = Trip.objects.filter(promoted=True)
        return context
