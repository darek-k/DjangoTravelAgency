from core.views import TripDetailsView, template_elements, hotels, about, blog_home, blog_single, \
    contact, insurance, ContinentCreateView, CountryCreateView, CityCreateView, AirportCreateView, \
    HotelCreateView, TripCreateView, AdminListView, ContinentDeleteView, AdminContinentDetailView, ContinentUpdateView, \
    AdminTripDetailView, AdminCityDetailView, AdminAirportDetailView, AdminHotelDetailView, AdminCountryDetailView, \
    CountryUpdateView, CityUpdateView, TripUpdateView, AirportUpdateView, HotelUpdateView, CountryDeleteView, \
    HotelDeleteView, AirportDeleteView, TripDeleteView, CityDeleteView
from django.urls import path

app_name = 'core'
urlpatterns = [
    path('trip_details/<pk>/', TripDetailsView.as_view(), name='trip_details'),

    path('elements/', template_elements, name='elements'),
    path('hotels/', hotels, name='hotels'),
    path('about/', about, name='about'),
    path('blog_home/', blog_home, name='blog_home'),
    path('blog_single/', blog_single, name='blog_single'),
    path('contact/', contact, name='contact'),
    path('insurance/', insurance, name='insurance'),
    # path('search_results/', TripSearchList, name='search_results'),

    path('add_continent/', ContinentCreateView.as_view(), name='add_continent'),
    path('add_country/', CountryCreateView.as_view(), name='add_country'),
    path('add_city/', CityCreateView.as_view(), name='add_city'),
    path('add_hotel/', HotelCreateView.as_view(), name='add_hotel'),
    path('add_airport/', AirportCreateView.as_view(), name='add_airport'),
    path('add_trip/', TripCreateView.as_view(), name='add_trip'),

    path('admin_list/', AdminListView.as_view(), name='admin_list'),

    path('admin_continent_details/<pk>/', AdminContinentDetailView.as_view(), name='admin_continent_details'),
    path('admin_country_details/<pk>/', AdminCountryDetailView.as_view(), name='admin_country_details'),
    path('admin_city_details/<pk>/', AdminCityDetailView.as_view(), name='admin_city_details'),
    path('admin_hotel_details/<pk>/', AdminHotelDetailView.as_view(), name='admin_hotel_details'),
    path('admin_airport_details/<pk>/', AdminAirportDetailView.as_view(), name='admin_airport_details'),
    path('admin_trip_details/<pk>/', AdminTripDetailView.as_view(), name='admin_trip_details'),

    path('continent_update/<pk>/', ContinentUpdateView.as_view(), name='continent_update'),
    path('country_update/<pk>/', CountryUpdateView.as_view(), name='country_update'),
    path('city_update/<pk>/', CityUpdateView.as_view(), name='city_update'),
    path('hotel_update/<pk>/', HotelUpdateView.as_view(), name='hotel_update'),
    path('airport_update/<pk>/', AirportUpdateView.as_view(), name='airport_update'),
    path('trip_update/<pk>/', TripUpdateView.as_view(), name='trip_update'),

    path('continent_delete/<pk>/', ContinentDeleteView.as_view(), name='continent_delete'),
    path('country_delete/<pk>/', CountryDeleteView.as_view(), name='country_delete'),
    path('city_delete/<pk>/', CityDeleteView.as_view(), name='city_delete'),
    path('hotel_delete/<pk>/', HotelDeleteView.as_view(), name='hotel_delete'),
    path('airport_delete/<pk>/', AirportDeleteView.as_view(), name='airport_delete'),
    path('trip_delete/<pk>/', TripDeleteView.as_view(), name='trip_delete')
]
