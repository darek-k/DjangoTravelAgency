from core.views import TripDetailsView, template_elements, hotels, about, blog_home, blog_single, \
    contact, insurance, packages, ContinentCreateView, CountryCreateView, CityCreateView, AirportCreateView, \
    HotelCreateView, TripCreateView
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
    path('packages/', packages, name='packages'),
    path('add_continent/', ContinentCreateView.as_view(), name='add_continent'),
    path('add_country/', CountryCreateView.as_view(), name='add_country'),
    path('add_city/', CityCreateView.as_view(), name='add_city'),
    path('add_hotel/', HotelCreateView.as_view(), name='add_hotel'),
    path('add_airport/', AirportCreateView.as_view(), name='add_airport'),
    path('add_trip/', TripCreateView.as_view(), name='add_trip'),
]
