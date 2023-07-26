from django.db import models

# Create your models here.
from django.db import models

class AnnualData(models.Model):
    api_well_number = models.CharField(max_length=20)
    oil = models.IntegerField()
    gas = models.IntegerField()
    brine = models.IntegerField()

    def __str__(self):
        return f"API Well Number: {self.api_well_number}"
