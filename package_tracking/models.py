from django.db import models

from .utils import CarrierService
# Create your models here.


class Package(models.Model):
    tracking_number = models.CharField(max_length=100, unique=True)
    service_name = models.CharField(max_length=5, choices=CarrierService.choices())
    status_text = models.CharField(max_length=200, default='Unknowm')
    status_date = models.DateField(blank=True, null=True)
