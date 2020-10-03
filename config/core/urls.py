from django.contrib import admin
from django.urls import path, include

from core.views import TripDetailsView

app_name = 'core'
urlpatterns = [
    path('trip/details/<pk>', TripDetailsView.as_view(), name='trip_details'),
    path()
]