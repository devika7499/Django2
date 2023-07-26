# import pandas as pd
# import sqlite3
# from sqlite_utils import Database
# from django.http import JsonResponse
# from django.views.decorators.http import require_http_methods
# from django.core.wsgi import get_wsgi_application
# from wsgiref.simple_server import make_server

# # Step 1: Download the Ohio Quarterly Production Data from Excel
# df = pd.read_excel('data.xls')

# # Step 2: Add up the quarterly data to calculate the annual data for oil, gas, and brine for each well based on API WELL NUMBER
# annual_data = df.groupby('API WELL  NUMBER').sum().to_dict()

# # Step 3: Using Python, load the calculated annual data into a local SQLite database
# conn = sqlite3.connect('annual_data.db')
# db = Database(conn)

# # Convert annual_data to the correct structure
# records = [{"key": str(key), **values} for key, values in annual_data.items()]

# # Create a table to store the annual data
# db["annual_data"].upsert_all(records, pk="key")


# # Step 4: Make an API using Django to allow for getting the annual data from the database using a GET request
# @require_http_methods(['GET'])
# def get_annual_data(request):
#     api_well_number = request.GET.get('well', '')

#     data = db['annual_data'].find_one(api_well_number=api_well_number)
#     if data is None:
#         return JsonResponse({'error': 'No data found for the specified well'}, status=404)

#     return JsonResponse(data)

# # Step 5: The app should be launchable by running: python main.py
# if __name__ == '__main__':
#     application = get_wsgi_application()
#     with make_server('', 8080, application) as server:
#         print('Server running on http://localhost:8080...')
#         server.serve_forever()


import os
import requests
import pandas as pd
import sqlite3
from django.core.wsgi import get_wsgi_application
from django.http import JsonResponse
from django.urls import path
from django.conf.urls import url

# Download the Ohio quarterly production data
url = 'https://ohiodnr.gov/static/documents/oil-gas/production/20110309_2020_1%20-%204.xls'
response = requests.get(url)

# Save the Excel file
with open('production_data.xls', 'wb') as file:
    file.write(response.content)

# Load the Excel file into a pandas DataFrame
data = pd.read_excel('production_data.xls')

# Calculate the annual production data
annual_data = data.groupby('API WELL NUMBER').sum()

# Convert the DataFrame to a dictionary
annual_data_dict = annual_data.to_dict()

# Load the annual data into a SQLite database
conn = sqlite3.connect('production.db')
cursor = conn.cursor()

# Create a table for the annual data
cursor.execute('''CREATE TABLE IF NOT EXISTS production (
                    well TEXT PRIMARY KEY,
                    oil INTEGER,
                    gas INTEGER,
                    brine INTEGER
                )''')

# Insert the annual data into the table
for well, production_data in annual_data_dict.items():
    oil = production_data['OIL']
    gas = production_data['GAS']
    brine = production_data['BRINE']
    cursor.execute('''INSERT INTO production (well, oil, gas, brine)
                      VALUES (?, ?, ?, ?)''', (well, oil, gas, brine))

# Commit the changes and close the connection
conn.commit()
conn.close()

# Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'production_api.settings')
application = get_wsgi_application()

# Django views
@require_GET
def get_annual_data(request):
    well = request.GET.get('well')

    # Connect to the SQLite database
    conn = sqlite3.connect('production.db')
    cursor = conn.cursor()

    # Retrieve the annual data for the specified well
    cursor.execute('''SELECT oil, gas, brine
                      FROM production
                      WHERE well = ?''', (well,))
    result = cursor.fetchone()

    # Close the database connection
    conn.close()

    if result:
        oil, gas, brine = result
        data = {
            'oil': oil,
            'gas': gas,
            'brine': brine
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Well not found'}, status=404)

# Django URLs
urlpatterns = [
    url(r'^data/$', get_annual_data),
]

if __name__ == '__main__':
    from django.core.management
