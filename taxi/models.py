from django.contrib.auth.models import AbstractUser
from django.db import models

from taxi_service import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    county = models.CharField(max_length=63)

    def __str__(self):
        return f"{self.name} country: {self.county}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.SET_NULL,
        null=True,
        related_name="cars"
    )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")

    def __str__(self):
        return f"{self.manufacturer.name}"
