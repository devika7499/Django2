

# Create your models here.
from django.db import models

class AnnualData(models.Model):
    API_WELL_NUMBER = models.CharField(max_length=20, primary_key=True)
    Oil = models.IntegerField()
    Gas = models.IntegerField()
    Brine = models.IntegerField()
