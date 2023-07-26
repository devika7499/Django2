from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import AnnualData


def get_annual_data(request):
    well_number = request.GET.get("well")

    try:
        annual_data = AnnualData.objects.get(API_WELL_NUMBER=well_number)
        response = {
            "oil": annual_data.OIL,
            "gas": annual_data.GAS,
            "brine": annual_data.BRINE
        }
        return JsonResponse(response)
    except AnnualData.DoesNotExist:
        return JsonResponse({"error": "Annual data not found."})

