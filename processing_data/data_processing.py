import requests
import pandas as pd
import sqlite3

# Step 1: Download the Excel file
# url = "https://ohiodnr.gov/static/documents/oil-gas/production/20110309_2020_1%20-%204.xls"
# response = requests.get(url)

# # Save the Excel file
# with open("production_data.xls", "wb") as file:
#     file.write(response.content)

# Step 2: Parse the Excel file and calculate annual data
# df = pd.read_excel("production_data.xls")
# df = pd.read_excel("production_data.xls", engine='openpyxl')
df = pd.read_excel('data.xls')


annual_data = df.groupby("API WELL  NUMBER").sum()
# annual_data.reset_index(inplace=True)
# annual_data["Annual Oil"] = annual_data["Quarter 1"] + annual_data["Quarter 2"] + annual_data["Quarter 3"] + annual_data["Quarter 4"]
# annual_data.drop(["Quarter 1", "Quarter 2", "Quarter 3", "Quarter 4"], axis=1, inplace=True)

# Step 3: Set up a local SQLite database and store the calculated annual data
conn = sqlite3.connect("production.db")
cursor = conn.cursor()

# Create a table for annual data
cursor.execute("CREATE TABLE IF NOT EXISTS annual_data (API WELL  NUMBER TEXT PRIMARY KEY, OIL INTEGER, GAS INTEGER, BRINE INTEGER)")

# # Insert the annual data into the database
# for _, row in annual_data.iterrows():
#     query = f"INSERT INTO annual_data (API WELL  NUMBER, OIL, GAS, BRINE) VALUES ('{row['API WELL  NUMBER']}', {row['OIL']}, {row['GAS']}, {row['BRINE']})"
#     cursor.execute(query)


# # Insert the annual data into the database
# for _, row in annual_data.iterrows():
#     query = f"INSERT INTO annual_data (`API WELL  NUMBER`, OIL, GAS, BRINE) VALUES ('{row['API WELL NUMBER']}', {row['Oil']}, {row['Gas']}, {row['Brine']})"
#     cursor.execute(query)

annual_data.to_sql("annual_data", conn, if_exists="replace", index=False)

# Commit the changes and close the connection
conn.commit()
conn.close()
