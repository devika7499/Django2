import pandas as pd
import sqlite3

# Load the Excel file
df = pd.read_excel('data.xls')

# Calculate annual data
annual_data = df.groupby('API WELL  NUMBER').sum()

# Save the annual data to SQLite database
conn = sqlite3.connect('db.sqlite3')
annual_data.to_sql('annualdata_welldata', conn, if_exists='replace')







