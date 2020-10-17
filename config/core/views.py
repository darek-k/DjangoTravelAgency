import datetime

# from accounts.models import Profile
from core.forms import ContinentForm, CountryForm, CityForm, HotelForm, AirportForm, TripForm, TripPurchaseForm
from core.models import Trip, Country, Continent, City, Hotel, Airport, Comment, TripPurchase
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from search_views.filters import BaseFilter
from search_views.views import SearchListView


def template_elements(request):
    return render(request, 'core/elements.html')


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


def render_initial_data(request):
    initial_data = {'name': 'Tu będzie nazwa kontynentu!'}
    obj = Trip.objects.get(id=1)
    form = CountryForm(request.POST or None, initial=initial_data, instance=obj)
    context = {'form': form}
    return render(request, 'form.html', context)


class TripDetailsView(DetailView):
    model = Trip
    template_name = 'core/trip_details.html'

    def get_context_data(self, **kwargs):
        context = super(TripDetailsView, self).get_context_data(**kwargs)
        context['form'] = TripPurchaseForm
        return context


class TripPurchaseCreateView(CreateView):
    # login_url = 'accounts:sign_in'
    form_class = TripPurchaseForm
    template_name = 'trip_purchase_form.html'
    success_url = reverse_lazy('trip_list')  # todo: strona z podsumowaniem płatności

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trip'] = Trip.objects.get(pk=self.kwargs.get('pk'))
        return context

    def get_initial(self):
        initial = super().get_initial()
        initial['trip'] = self.kwargs.get('pk')

        initial['main_booker'] = self.request.user.id
        initial['adults_number'] = 0
        initial['kids_number'] = 0
        initial['final_price'] = 1000
        initial['test_char_field'] = 'test - czy sie zapisze??'
        return initial


class TripCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'core.add_trip'

    title = 'Add trip'
    template_name = 'form.html'
    form_class = TripForm
    success_url = reverse_lazy('core:admin_list')

    def get_initial(self):
        initial = super().get_initial()
        initial['departure_city'] = 3
        initial['price_for_adult'] = 12345
        initial['promoted'] = True
        return initial


class ContinentCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'core.add_continent'
    title = 'Add continent'
    template_name = 'form.html'
    form_class = ContinentForm
    success_url = reverse_lazy('core:admin_list')


class TripListView(ListView):
    model = Trip
    template_name = 'core/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TripListView, self).get_context_data(**kwargs)
        context['all_trips'] = Trip.objects.all()
        context['promoted_trips'] = Trip.objects.filter(promoted=True)[:3]
        context['last_minute_trips'] = Trip.objects.filter(departure_date__lt=now() + datetime.timedelta(30))[:3]
        context['all_countries'] = Country.objects.exclude(name='Polska')
        context['all_comments'] = Comment.objects.all()
        context['today'] = datetime.datetime.now()
        # context['prices'] = [i.price_for_adult for i in Trip.objects.all() if i.arrival_city.country.name=="Hiszpania"]
        return context


class HotelListView(ListView):
    model = Hotel
    template_name = 'core/hotels.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HotelListView, self).get_context_data()
        context['hotels'] = Hotel.objects.order_by('-stars')
        return context


class AdditionalServicesView(ListView):
    model = Comment
    template_name = 'core/additional_services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['all_comments'] = Comment.objects.all()
        return context


class AdminListView(PermissionRequiredMixin, ListView):
    permission_required = 'core.view_trip'
    model = Trip
    template_name = 'core/admin_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AdminListView, self).get_context_data(**kwargs)
        context['continents'] = Continent.objects.all()
        context['countries'] = Country.objects.all()
        context['cities'] = City.objects.all()
        context['hotels'] = Hotel.objects.all()
        context['airports'] = Airport.objects.all()
        context['trips'] = Trip.objects.all()
        return context


class CountryCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'core.add_country'

    title = 'Add country'
    template_name = 'form.html'
    form_class = CountryForm
    success_url = reverse_lazy('core:admin_list')


class CityCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'core.add_city'

    title = 'Add city'
    template_name = 'form.html'
    form_class = CityForm
    success_url = reverse_lazy('core:admin_list')


class HotelCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'core.add_hotel'

    title = 'Add hotel'
    template_name = 'form.html'
    form_class = HotelForm
    success_url = reverse_lazy('core:admin_list')


class AirportCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'core.add_airport'

    title = 'Add airport'
    template_name = 'form.html'
    form_class = AirportForm
    success_url = reverse_lazy('core:admin_list')


class AdminContinentDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'core.view_continent'

    model = Continent
    template_name = 'core/admin_continent_details.html'


class ContinentUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'core.change_continent'

    model = Continent
    template_name = 'edit_form.html'
    form_class = ContinentForm
    success_url = reverse_lazy('core:admin_list')


class ContinentDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'core.delete_continent'

    model = Continent
    template_name = 'delete_form.html'
    form_class = ContinentForm
    success_url = reverse_lazy('core:admin_list')


class AdminCountryDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'core.view_country'

    model = Country
    template_name = 'core/admin_country_details.html'


class CountryUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'core.change_country'

    model = Country
    template_name = 'edit_form.html'
    form_class = CountryForm
    success_url = reverse_lazy('core:admin_list')


class CountryDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'core.delete_country'

    model = Country
    template_name = 'delete_form.html'
    form_class = CountryForm
    success_url = reverse_lazy('core:admin_list')


class AdminCityDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'core.view_city'

    model = City
    template_name = 'core/admin_city_details.html'


class CityUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'core.change_city'

    model = City
    template_name = 'edit_form.html'
    form_class = CityForm
    success_url = reverse_lazy('core:admin_list')


class CityDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'core.delete_city'

    model = City
    template_name = 'delete_form.html'
    form_class = CityForm
    success_url = reverse_lazy('core:admin_list')


class AdminHotelDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'core.view_hotel'

    model = Hotel
    template_name = 'core/admin_hotel_details.html'


class HotelUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'core.change_hotel'

    model = Hotel
    template_name = 'edit_form.html'
    form_class = HotelForm
    success_url = reverse_lazy('core:admin_list')


class HotelDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'core.delete_hotel'

    model = Hotel
    template_name = 'delete_form.html'
    form_class = HotelForm
    success_url = reverse_lazy('core:admin_list')


class AdminAirportDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'core.view_airport'

    model = Airport
    template_name = 'core/admin_airport_details.html'


class AirportUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'core.change_airport'

    model = Airport
    template_name = 'edit_form.html'
    form_class = AirportForm
    success_url = reverse_lazy('core:admin_list')


class AirportDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'core.delete_airport'

    model = Airport
    template_name = 'delete_form.html'
    form_class = AirportForm
    success_url = reverse_lazy('core:admin_list')


class AdminTripDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'core.view_trip'

    model = Trip
    template_name = 'core/admin_trip_details.html'


class TripUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'core.change_trip'

    model = Trip
    template_name = 'edit_form.html'
    form_class = TripForm
    success_url = reverse_lazy('core:admin_list')


class TripDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'core.delete_trip'

    model = Trip
    template_name = 'delete_form.html'
    form_class = TripForm
    success_url = reverse_lazy('core:admin_list')


class SearchResultsView(ListView):
    model = Trip
    template_name = 'core/search_results.html'

    def get_queryset(self):
        if self.request.GET.get('country'):
            q_country = self.request.GET.get('country')
            print(q_country)
            search_results = Trip.objects.filter(
                Q(arrival_city__country__name__icontains=q_country)
            )

        else:
            q_to = self.request.GET.get('to')
            q_from = self.request.GET.get('from')
            q_date = self.request.GET.get('date')
            print(q_to, q_from)
            search_results = Trip.objects.filter(
                (Q(arrival_city__name__icontains=q_to) | Q(arrival_city__country__name__icontains=q_to)) & Q(
                    departure_city__name__icontains=q_from) & Q(
                    departure_date__gt=q_date)
            )

        return search_results
