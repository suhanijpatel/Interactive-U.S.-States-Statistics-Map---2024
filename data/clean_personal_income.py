import pandas as pd

#file path for personal income data CSV
file_path = 'personal-income-data.csv'
#read file into DataFrame
data = pd.read_csv(file_path)

#filter data to only include rows with relevant Description value
personal_income_data = data[data['Description'].str.contains('Personal income (millions of dollars)', case=False, na=False, regex=False)]

#keeping columns with following identifiers for years 2003 - 2023
columns_to_keep = ['GeoFIPS', 'GeoName', 'Region', 'Description'] + [str(year) for year in range(2000, 2024)]

#filter previously filtered rows to only include columns we want
filtered_data = personal_income_data[columns_to_keep]

#write to new file
filtered_data.to_csv('cleaned-personal-income.csv', index=False)

