from django.shortcuts import render

# Create your views here.
import pandas as pd
from django.shortcuts import render
from .models import Well

def process_production_data(request):
    # Load the Excel file
    file_path = '20210309_2020_1 - 4.xls'
    df = pd.read_excel(file_path)

    # Group by API WELL NUMBER and calculate annual production
    grouped_data = df.groupby('API WELL  NUMBER').sum()

    # Iterate over the grouped data and save to the database
    for api_well_number, row in grouped_data.iterrows():
        well = Well.objects.create(
            api_well_number=api_well_number,
            oil_production=row['OIL'],
            gas_production=row['GAS'],
            brine_production=row['BRINE']
        )
        well.save()

    return render(request, 'success.html')
