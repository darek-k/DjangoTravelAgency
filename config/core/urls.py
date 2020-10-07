from core.views import TripDetailsView, template_elements, hotels, about, blog_home, blog_single, contact, insurance, \
    packages
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
]
