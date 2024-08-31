from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # if the field in database is null it's ok and if its blank on user form also ok
    age = models.PositiveIntegerField(null=True, blank=True)
    photo = models.ImageField(upload_to='photo/profile/%Y/%m/%d/', default='null')
    about = models.CharField(max_length=255, default='null')
