import pandas as pd

file_path = 'consumer-spending-data.csv'
data = pd.read_csv(file_path)

filtered_data = data[
    data['Description'].str.strip().str.lower().isin([
        "personal consumption expenditures",
        "household consumption expenditures"
    ])
]

columns_to_keep = ['GeoName', 'Region', 'Description'] + [str(year) for year in range(2000, 2024)]
filtered_data = filtered_data[columns_to_keep]

output_path = 'cleaned-consumer-spending.csv'
filtered_data.to_csv(output_path, index=False)

print(f"Filtered data saved to {output_path}")
