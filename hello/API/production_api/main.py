import urllib.request
from django.urls import include, path
from data_api.views import get_annual_data


url = 'https://ohiodnr.gov/static/documents/oil-gas/production/20210309_2020_1%20-%204.xls'
file_path = 'production_data.xls'

urllib.request.urlretrieve(url, file_path)
import pandas as pd

# Read the Excel file
df = pd.read_excel('production_data.xls')

# Group the data by API WELL NUMBER and calculate the sum for each quarter
annual_data = df.groupby('API WELL  NUMBER')['OIL', 'GAS', 'BRINE'].sum()

# Convert the DataFrame to a dictionary for easier access
annual_data_dict = annual_data.to_dict()


import sqlite3

# Connect to the database
conn = sqlite3.connect('production_data.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table to store the annual data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS annual_data (
        well_id TEXT PRIMARY KEY,
        oil INTEGER,
        gas INTEGER,
        brine INTEGER
    )
''')

# Insert the data into the table
for well_id, data in annual_data_dict.items():
    oil = data['OIL']
    gas = data['GAS']
    brine = data['BRINE']
    cursor.execute('''
        INSERT INTO annual_data (well_id, oil, gas, brine)
        VALUES (?, ?, ?, ?)
    ''', (well_id, oil, gas, brine))

# Commit the changes and close the connection
conn.commit()
conn.close()
