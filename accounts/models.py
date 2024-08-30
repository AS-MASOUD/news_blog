from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # if the field in database is null its ok and if its blank on user form also ok
    age = models.PositiveIntegerField(null=True, blank=True)
