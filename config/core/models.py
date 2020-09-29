from django.db import models

STARS_CHOICES = [
    ('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6)
]

CATERING_OPTIONS = [
    ('BB', 'bed & breakfast'), ('HB', 'half board'), ('FB', 'full board'), ('Al', 'all inclusive'), ('OV', 'overnight'),
    ('SC', 'self catering'), ('PP', 'program package'), ('ZPR', 'ZPR')
]


class Continent(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE, related_name='countries')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    stars = models.CharField(max_length=1, choices=STARS_CHOICES, default=1)
    description = models.TextField(max_length=1000, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='hotels')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Airport(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='airports')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Trip(models.Model):
    departure_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='departure_city_trips')
    departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departure_airport_trips')
    arrival_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='arrival_city_trips')
    arrival_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='arrival_hotel_trips')
    arrival_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrival_airport_trips')
    date_of_departure = models.DateTimeField()
    date_of_arrival = models.DateTimeField()
    date_of_return = models.DateTimeField()
    days = models.DurationField()
    catering_option = models.CharField(choices=CATERING_OPTIONS, max_length=20)
    price_for_adult = models.DecimalField(decimal_places=2, max_digits=6)
    price_for_child = models.DecimalField(decimal_places=2, max_digits=6)
    promoting = models.BooleanField(default=False)
    adults_number = models.IntegerField(default=0)
    kids_number = models.IntegerField(default=0)


class TripPurchase(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='trips_purchases')
    participants_data = models.CharField(max_length=1000)
    price = models.DecimalField(decimal_places=2, max_digits=6)
