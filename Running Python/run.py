
import os
import pandas as pd
import sys


# Add the folder path to the sys.path
sys.path.append('C:/Users/Sedláček/pr/Project-Weather-electricity-prices/Data')

# Now you can import functions from other modules
from Weather_data_preparation import process_and_merge_weather_data
from Data_merge import merge_and_process_data
# Call the function

# Path to the new working directory
new_directory = "C:/Users/Sedláček/pr/Project-Weather-electricity-prices/Data"

# Changing the current working directory
os.chdir(new_directory)


weather_base = 'Weather_base.xlsx'    
weather_new = 'Weather_new.csv'

process_and_merge_weather_data(weather_base, weather_new)

weather_data_path = 'All_weather_data.csv'
value_data_path = 'Value.csv'
output_file_path = 'final_data.csv'

merge_and_process_data(weather_data_path, value_data_path, output_file_path)