from django.db import models
from datetime import datetime


class Cities(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Streets(models.Model):
    name = models.CharField(max_length=32, unique=True)
    city = models.ForeignKey(to=Cities, on_delete=models.CASCADE)

    def __str__(self):
        return f'street {self.name} in city {self.city.name}'


class Shops(models.Model):
    name = models.CharField(max_length=32, unique=True)
    city = models.ForeignKey(to=Cities, on_delete=models.CASCADE)
    street = models.ForeignKey(to=Streets, on_delete=models.CASCADE)
    house = models.PositiveSmallIntegerField()
    opening_time = models.PositiveSmallIntegerField(default=9)
    closing_time = models.PositiveSmallIntegerField(default=21)

    def __str__(self):
        return f'shop {self.name} in city {self.city} on street {self.street}'



