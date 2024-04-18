from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

class Car(models.Model):
    category = models.CharField(max_length=32)
    marka = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    price = models.CharField(max_length=32)
    year = models.SmallIntegerField
    mileage = models.PositiveIntegerField
    city = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    with_photo = models.BooleanField
    color = models.CharField(max_length=32)
    volume = models.FloatField
    description = models.TextField


class Bet(models.Model):
    number = models.IntegerField
    total_number = models.IntegerField
    buy_now = models.IntegerField
