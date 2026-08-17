from django.contrib import admin
from .models import Bike


@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'brand',
        'price',
        'engine',
        'mileage',
        'power',
        'torque',
        'top_speed',
        'brakes_abs',
    )

    search_fields = (
        'name',
        'brand',
    )