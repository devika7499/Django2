from django.db import models

# Create your models here.
from django.db import models

class Well(models.Model):
    api_well_number = models.CharField(max_length=50)
    oil_production = models.IntegerField()
    gas_production = models.IntegerField()
    brine_production = models.IntegerField()

