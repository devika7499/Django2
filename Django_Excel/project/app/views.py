from django.shortcuts import render

# Create your views here.
from .models import WellData
from tablib import Dataset
from .resources import DataResources


def importExcel(request):
    if request.method=='POST':
        data_resource=DataResources()
        dataset=Dataset()
        new_data=request.FILES['my_file']
        imported_data=dataset.load(new_data.read())
        for data in imported_data:
            value=WellData(data[0],data[8],data[9],data[10])
            value.save()
    return render(request,'form.html')
