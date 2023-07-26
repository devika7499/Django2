from import_export import resources
from .models import WellData

class DataResources(resources.ModelResource):
    class Meta:
        model=WellData