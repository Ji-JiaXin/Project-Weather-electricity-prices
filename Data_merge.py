# Weather preparation
import pandas as pd

import os
# Path to the new working directory
new_directory = "C:/Users/Sedláček/pr/Project-Weather-electricity-prices"

# Change the current working directory
os.chdir(new_directory)

# Verify the change
print("New working directory:", os.getcwd())

# Replace with your actual file paths
weather_data = 'Weather_data' 
Elcet_gen_onshore_wind = 'Elcet_gen_onshore_wind.csv'

# Load the files
data_1 = pd.read_csv(weather_data)
data_2 = pd.read_csv(Elcet_gen_onshore_wind)

# Merge the files on the 'Date' column
merged_data = pd.merge(data_1, data_2, on='Date', how='inner')
print(merged_data)

# Remove duplicate rows
merged_data = merged_data.drop_duplicates()

# Group by the 'Date' column and average the 'Value' column
# Replace 'Date' and 'Value' with the actual column names from your dataset
merged_data = merged_data.groupby('Date', as_index=False).mean()

merged_data['Temperature'] = merged_data['Temperature'].round(1)

# Save the merged data to a new file
merged_data.to_csv('merged_file.csv', index=False)
