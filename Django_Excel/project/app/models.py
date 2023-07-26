from django.db import models


# Create your models here.
from django.db import models

class WellData(models.Model):
    api_well_number = models.CharField(max_length=50)
    oil = models.FloatField(blank=True,
   default=00000)
    gas = models.FloatField(blank=True,
   default=00000)
    brine = models.FloatField(blank=True,
   default=00000)
    
    