import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'production_api.settings')
django.setup()

import pandas as pd



from production_data.models import AnnualData  # Replace 'your_app' with your app name


import requests

# url = "https://ohiodnr.gov/static/documents/oil-gas/production/20110309_2020_1%20-%204.xls"
# response = requests.get(url)

# # Save the file to your desired location
# with open("ohio_production_data.xls", "wb") as file:
#     file.write(response.content)
import pandas as pd

# Read the Excel file
# data = pd.read_excel("ohio_production_data.xls")
data = pd.read_excel('data.xls')
# print(data.head())


# Group the data by API WELL NUMBER and sum the quarterly production values
annual_data = data.groupby("API WELL  NUMBER").sum()

# Convert the result to a dictionary
annual_data_dict = annual_data.to_dict()



import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("annual_data.db")
cursor = conn.cursor()

# Create a table for the annual data
cursor.execute("CREATE TABLE IF NOT EXISTS annual_data (api_well_number TEXT, oil INTEGER, gas INTEGER, brine INTEGER)")

# Iterate over the annual data and insert it into the database
# Iterate over the annual data and calculate the annual values
# annual_data_dict = {}
# for api_well_number, row in annual_data.iterrows():
#     oil = row["OIL"]
#     gas = row["GAS"]
#     brine = row["BRINE"]
#     annual_data_dict[api_well_number] = {
#         "oil": oil,
#         "gas": gas,
#         "brine": brine
#     }
#     annual_data_obj = AnnualData(api_well_number=api_well_number, oil=oil, gas=gas, brine=brine)
#     annual_data_obj.save()
# Iterate over the annual data and calculate the annual values
annual_data_dict = {}
for api_well_number, row in annual_data.iterrows():
    oil = row["OIL"]
    gas = row["GAS"]
    brine = row["BRINE"]
    annual_data_dict[api_well_number] = {
        "oil": oil,
        "gas": gas,
        "brine": brine
    }
    

    # Insert the values into the database
    try:
        AnnualData.objects.create(api_well_number=api_well_number, oil=oil, gas=gas, brine=brine)
    except Exception as e:
        print(f"Error inserting values for API well number {api_well_number}: {str(e)}")
for api_well_number, data in annual_data_dict.items():
    oil = data["oil"]
    gas = data["gas"]
    brine = data["brine"]
    annual_data = AnnualData(api_well_number=api_well_number, oil=oil, gas=gas, brine=brine)
    annual_data.save()
# Commit the changes and close the connection
conn.commit()
conn.close()
