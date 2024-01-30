# Example input: 5, 6, 7, 8, 2, 4, 2, 7
import os
import pandas as pd

# Path to the new working directory
new_directory = "C:/Users/Sedláček/pr/Project-Weather-electricity-prices/Data"

# Changing the current working directory
os.chdir(new_directory)

file_path = 'Weather_base.xlsx'    # Replace with your actual file path
csv_file_path = 'Weather_new.csv'  # Same

process_and_merge_weather_data(file_path, csv_file_path)

# Usage example:
weather_data_path = 'weather_data.csv'  
value_data_path = 'Value.csv'      
output_file_path = 'merged_data.csv'           

merge_and_process_data(weather_data_path, value_data_path, output_file_path)

from Searching_first_diff import *




