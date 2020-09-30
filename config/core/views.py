import datetime

from core.models import Trip
from django.utils.timezone import now
from django.views.generic import ListView, DetailView


class TripDetailsView(DetailView):
    model = Trip
    template_name = 'core/trip_details.html'



# todo: Lepiej jest trzymać contexty w jednej klasie czy to rozdzielić? Jak miałem rozdzielone to nie wyświetał się context z klasy poniżej.
class TripListView(ListView):
    model = Trip
    template_name = 'core/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['promoted_trips'] = Trip.objects.filter(promoted=True)
        context['last_minute_trips'] = Trip.objects.filter(departure_date__lt=now()+datetime.timedelta(30))
        return context


# todo: Nie wyświetla się ten widok. DLaczego?:
# class LastMinuteView(ListView):
#     model = Trip
#     template_name = 'core/index.html'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data()
#         context['last_minute_trips'] = Trip.objects.all()
#         return context
