import pandas as pd

#file path for consumer spending CSV
file_path = 'consumer-spending-data.csv'
data = pd.read_csv(file_path)

#filter data to only include rows with relevant Description value
filtered_data = data[
    data['Description'].str.strip().str.lower().isin([
        "personal consumption expenditures",
        "household consumption expenditures"
    ])
]

#keeping columns with following identifiers for years 2003 - 2023
columns_to_keep = ['GeoName', 'Region', 'Description'] + [str(year) for year in range(2000, 2024)]
#filter previously filtered rows to only include columns we want
filtered_data = filtered_data[columns_to_keep]

#write to new file
output_path = 'cleaned-consumer-spending.csv'
filtered_data.to_csv(output_path, index=False)

print(f"Filtered data saved to {output_path}")