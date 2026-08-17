from django.db import models


class Bike(models.Model):

    name = models.CharField(max_length=100)

    brand = models.CharField(max_length=50)

    price = models.CharField(max_length=100)

    engine = models.CharField(max_length=50)

    mileage = models.CharField(max_length=50)

    power = models.CharField(max_length=50, blank=True, null=True)

    torque = models.CharField(max_length=50, blank=True, null=True)

    top_speed = models.CharField(max_length=50, blank=True, null=True)

    brakes_abs = models.CharField(max_length=100, blank=True, null=True)

    pros_cons_rating = models.TextField(blank=True, null=True)

    image = models.ImageField(
        upload_to='bikes/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name