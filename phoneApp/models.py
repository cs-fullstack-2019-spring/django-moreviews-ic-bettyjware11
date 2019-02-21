from django.db import models

# Create your models here.
class Phone(models.Model):
    name = models.CharField(max_length=200, default="")
    hoursOfBattery = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)
    version = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)