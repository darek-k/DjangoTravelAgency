from django.db import models

STARS_CHOICES = [
    (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)
]


class Continent(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    stars = models.CharField(max_length=1, choices=STARS_CHOICES, default=1)
    description = models.TextField(max_length=1000, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Airport(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Trip(models.Model):
    #todo - create class
    pass


class TripPurchase(models.Model):
    #todo - create class
    pass
