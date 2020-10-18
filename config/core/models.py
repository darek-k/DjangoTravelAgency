from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone

STARS_CHOICES = [
    (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'),
]

CATERING_OPTIONS = [
    ('Bed & Breakfast', 'BB'), ('Half board', 'HB'), ('Full board', 'FB'), ('All inclusive', 'Al'), ('Overnight', 'OV'),
    ('Self catering', 'SC'), ('Program package', 'PP'), ('ZPR', 'ZPR')
]

BOOL_OPTIONS = [
    ('Tak', 'Tak'), ('Nie', 'Nie')
]

RATING = [
    (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')
]


def get_city_image_path(instance, filename):
    return f'static/core/photos/city_{instance.id}/{filename}'


def get_hotel_image_path(instance, filename):
    return f'static/core/photos/hotel_{instance.id}/{filename}'


def get_country_image_path(instance, filename):
    return f'static/core/photos/country_{instance.id}/{filename}'


class Continent(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE, related_name='countries')
    country_image = models.ImageField(upload_to=get_country_image_path, null=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'countries'

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities')
    city_image = models.FileField(upload_to=get_city_image_path, null=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    stars = models.IntegerField(choices=STARS_CHOICES, default=1)
    description = models.TextField(max_length=2000, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='hotels')
    location = models.CharField(default='', max_length=500, null=True)
    swimming_pool = models.CharField(choices=BOOL_OPTIONS, default='Nie', max_length=10)
    wifi = models.CharField(choices=BOOL_OPTIONS, default='Nie', max_length=10)
    air_condition = models.CharField(choices=BOOL_OPTIONS, default='Nie', max_length=10)
    room_service = models.CharField(choices=BOOL_OPTIONS, default='Nie', max_length=10)
    restaurant = models.CharField(choices=BOOL_OPTIONS, default='Nie', max_length=10)
    gym = models.CharField(choices=BOOL_OPTIONS, default='Nie', max_length=10)
    hotel_image = models.FileField(upload_to=get_hotel_image_path, null=True)
    hotel_image2 = models.FileField(upload_to=get_hotel_image_path, null=True)

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

    departure_date = models.DateTimeField()
    arrival_date = models.DateTimeField()
    return_date = models.DateTimeField()
    back_home_date = models.DateTimeField(null=True)

    # todo: jak to odjąć? Na obiekcie nie ma żadnych problemów z odejmowaniem tych dwóch wartości
    # duration = return_date-arrival_date

    catering_option = models.CharField(choices=CATERING_OPTIONS, max_length=20)
    price_for_adult = models.DecimalField(decimal_places=0, max_digits=6)
    price_for_child = models.DecimalField(decimal_places=0, max_digits=6)
    promoted = models.BooleanField(default=False)
    comment = models.ManyToManyField

    def __str__(self):
        return f"Z: {self.departure_city} do: {self.arrival_city} - {self.arrival_hotel}. Data wyjazdu: {self.departure_date} " \
               f"Data odlotu: {self.return_date}"


class TripPurchase(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='trips')
    main_booker = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    adults_number = models.IntegerField(default=0, validators=[MinValueValidator(1),])
    kids_number = models.IntegerField(default=0, blank=True)
    final_price = models.DecimalField(decimal_places=2, max_digits=6)
    test_char_field = models.CharField(max_length=50, default='', blank=True)


class Comment(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, null=True, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    text = models.TextField(max_length=1000)
    rating = models.IntegerField(choices=RATING)
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('created_date',)

    def __str__(self):
        return f'Comment: "{self.text}" created by {self.author}'
