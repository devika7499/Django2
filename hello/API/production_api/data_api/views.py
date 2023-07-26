from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import sqlite3

def get_annual_data(request):
    well_id = request.GET.get('well')
    conn = sqlite3.connect('production_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT oil, gas, brine FROM annual_data WHERE well_id = ?
    ''', (well_id,))
    result = cursor.fetchone()
    conn.close()
