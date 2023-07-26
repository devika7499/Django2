from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import WellData


def get_annual_data(request):
    api_well_number = request.GET.get('well')
    try:
        well_data = WellData.objects.get(api_well_number=api_well_number)
        response = {
            'oil': well_data.oil,
            'gas': well_data.gas,
            'brine': well_data.brine
        }
    except WellData.DoesNotExist:
        response = {}  # Empty response if well data is not found
    return JsonResponse(response)