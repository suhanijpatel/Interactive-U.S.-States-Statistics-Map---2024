import pandas as pd

#file path for GDP data CSV
file_path = 'summary_bls_data.csv'
data = pd.read_csv(file_path)

#filter data to only include rows with relevant Description value
gdp_data = data[data['Description'].str.contains('Gross domestic product', case=False, na=False)]

#keeping columns with following identifiers for years 2003 - 2023
columns_to_keep = ['GeoFIPS', 'GeoName', 'Region', 'Description', ] + [str(year) for year in range(2000, 2024)]

#filter previously filtered rows to only include columns we want
filtered_gdp_data = gdp_data[columns_to_keep]

#write to new file
filtered_gdp_data.to_csv('cleaned-gdp.csv', index=False)
