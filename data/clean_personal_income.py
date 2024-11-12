import pandas as pd

file_path = 'personal-income-data.csv'
data = pd.read_csv(file_path)

personal_income_data = data[data['Description'].str.contains('Personal income (millions of dollars)', case=False, na=False, regex=False)]

columns_to_keep = ['GeoFIPS', 'GeoName', 'Region', 'Description'] + [str(year) for year in range(2000, 2024)]
filtered_data = personal_income_data[columns_to_keep]

filtered_data.to_csv('cleaned-personal-income.csv', index=False)

