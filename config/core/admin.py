from django.contrib import admin

# Register your models here.
from core.models import Continent, Country, City, Airport, Hotel

admin.site.register(Continent)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Airport)
admin.site.register(Hotel)
# admin.site.register(Trip)
# admin.site.register(TripPurchase)