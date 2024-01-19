## Merginf the data about weather and from the API

import pandas as pd
import os

# Path to the new working directory, can be adjust as needed
new_directory = "C:/Users/Sedláček/pr/Project-Weather-electricity-prices"

# Change the current working directory
os.chdir(new_directory)

# Verify the change
print("New working directory:", os.getcwd())

# Replaceable as needed
weather_data = 'Weather_data' 
Value = 'Value.csv'

# Loading the files
data_1 = pd.read_csv(weather_data)
data_2 = pd.read_csv(Value)

# Merge the files on the 'Date' column
# Data for certain day have to be connected together
merged_data = pd.merge(data_1, data_2, on='Date', how='inner')

# Checking the data
print(merged_data)

# Remove duplicate rows
merged_data = merged_data.drop_duplicates()

# Group by the 'Date' column and average the 'Value' column
# Replacing 'Date' and 'Value' with the actual column names from your dataset
merged_data = merged_data.groupby('Date', as_index=False).mean()
merged_data['Temperature'] = merged_data['Temperature'].round(1)


# Saving the merged data to a new file
merged_data.to_csv('merged_file.csv', index=False)

# Now we have all the data prepared