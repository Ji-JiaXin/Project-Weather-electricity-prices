# Searching for similar temperatures
import pandas as pd
import numpy as np
import os
# Path to the new working directory
new_directory = "C:/Users/Sedláček/pr/Project-Weather-electricity-prices"

# Change the current working directory
os.chdir(new_directory)

# Verify the change
print("New working directory:", os.getcwd())


def find_similar_temperature_period(input_temperatures, data):
    """
    Find the 7-day period in the data where the temperatures are most similar to the given input temperatures.
    
    Parameters:
    input_temperatures (list of float): A list of 7 temperatures.
    data (pd.DataFrame): The dataframe with the temperature data.

    Returns:
    pd.DataFrame: A dataframe of the 7-day period with the most similar temperatures.
    """
    if len(input_temperatures) != 7:
        raise ValueError("Input temperatures must be a list of 7 numbers.")

    min_diff = np.inf
    best_start_date = None

    for i in range(len(data) - 6):
        current_period = data.iloc[i:i+7]
        current_temperatures = current_period['Temperature'].tolist()
        diff = sum((np.array(current_temperatures) - np.array(input_temperatures))**2)

        if diff < min_diff:
            min_diff = diff
            best_start_date = current_period.iloc[0]['Date']

    if best_start_date is not None:
        best_period_index = data[data['Date'] == best_start_date].index[0]
        return data.iloc[best_period_index:best_period_index+7]
    else:
        return None

def get_temperature_input():
    while True:
        try:
            input_string = input("Enter 7 temperatures separated by commas: ")
            temperatures = [float(temp.strip()) for temp in input_string.split(",")]

            if len(temperatures) != 7:
                raise ValueError("Exactly 7 temperatures are required.")
            
            return temperatures
        except ValueError as e:
            print("Invalid input. Please enter 7 numbers separated by commas. Error:", e)

# Load the merged file
file_path = 'merged_file.csv'  
merged_data = pd.read_csv(file_path)

# Prompt user for temperature input
input_temperatures = get_temperature_input()

# Find the most similar temperature period
similar_period = find_similar_temperature_period(input_temperatures, merged_data)
print(similar_period)
