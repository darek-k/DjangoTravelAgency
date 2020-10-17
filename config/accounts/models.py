from django.contrib.auth.models import User
from django.db import models


class Profile(User):
    purchased_trips = []

    class Meta:
        proxy = True
