from django.db import models

# Create your models here.
from django.db import models

class WellData(models.Model):
    api_well_number = models.CharField(max_length=50)
    oil = models.FloatField()
    gas = models.FloatField()
    brine = models.FloatField()
    
    class Meta:
        managed = False
        db_table = 'annualdata_welldata'
        
    def __str__(self):
        return self.api_well_number