from django.contrib import admin
from django.urls import path, include

from core.views import TripDetailsView, template_elements, hotels

app_name = 'core'
urlpatterns = [
    path('trip_details/<pk>/', TripDetailsView.as_view(), name='trip_details'),
    path('elements/', template_elements, name='template_elements'),
    path('hotels/', hotels, name='hotels'),
]
