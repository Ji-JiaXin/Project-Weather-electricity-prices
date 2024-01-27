# Run try
# Weather prep
import os
import pandas as pd

# Path to the new working directory
new_directory = "C:/Users/Sedláček/pr/Project-Weather-electricity-prices/Data"

# Changing the current working directory
os.chdir(new_directory)

# Verifing the change
print("New working directory:", os.getcwd())


file_path = 'Weather_base.xlsx'  
csv_file_path = 'Weather_new.csv'  # Replace with your actual file path

from Weather_data_preparation import *

process_and_merge_weather_data(file_path, csv_file_path)


# Usage example:
weather_data_path = 'weather_data.csv'  
value_data_path = 'Value.csv'      
output_file_path = 'merged_data.csv'           

from Data_merge import *

merge_and_process_data(weather_data_path, value_data_path, output_file_path)







