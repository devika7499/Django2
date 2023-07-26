from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import sqlite3


def get_annual_data(request):
    api_well_number = request.GET.get("well")

    # Connect to the SQLite database
    conn = sqlite3.connect("annual_data.db")
    cursor = conn.cursor()

    # Retrieve the annual data for the specified well
    cursor.execute("SELECT oil, gas, brine FROM annual_data WHERE api_well_number=?", (api_well_number,))
    result = cursor.fetchone()

    # Close the database connection
    conn.close()

    if result is None:
        # Well not found in the database
        return JsonResponse({"error": "Well not found"})

    # Construct the JSON response
    oil, gas, brine = result
    response = {
        "oil": oil,
        "gas": gas,
        "brine": brine
    }

    return JsonResponse(response)
