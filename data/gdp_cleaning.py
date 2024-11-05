import json
import pandas as pd
file_path = 'summary_bls_data.csv'
data = pd.read_csv(file_path)

gdp_data = data[data['Description'].str.contains('Gross domestic product', case=False, na=False)]
employment_data=data[data['Description'].str.contains('Gross domestic product', case=False, na=False)]
columns_to_keep = ['GeoFIPS', 'GeoName', 'Region', 'Description', ] + [str(year) for year in range(2000, 2024)]

filtered_gdp_data = gdp_data[columns_to_keep]
filtered_employment_data = employment_data[columns_to_keep]

filtered_gdp_data.to_csv('cleaned-gdp.csv', index=False)
filtered_employment_data.to_csv= employment_data[columns_to_keep]

