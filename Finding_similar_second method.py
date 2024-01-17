# Second try for finding similar values

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


def find_similar_temperature_periods(input_temperatures, data, threshold):
    """
    Find all 7-day periods in the data where the temperatures are similar to the given input temperatures within a threshold.
    
    Parameters:
    input_temperatures (list of float): A list of 7 temperatures.
    data (pd.DataFrame): The dataframe with the temperature data.
    threshold (float): The maximum allowed sum of squared differences to consider periods as similar.

    Returns:
    list of pd.DataFrame: A list of dataframes, each representing a 7-day period with similar temperatures.
    """
    if len(input_temperatures) != 7:
        raise ValueError("Input temperatures must be a list of 7 numbers.")

    #initializing an empty list
    similar_periods = []

    # Iterating through the 'Data' and checking 7-day periods
    for i in range(len(data) - 6):
        """ For each period, calculate the sum of square diff. between
           # Temperatures and input numbers
           """
        current_period = data.iloc[i:i+7]
        current_temperatures = current_period['Temperature'].tolist()
        diff = sum((np.array(current_temperatures) - np.array(input_temperatures))**2)

        """ If the sum is less then 'treshold' then add the time period
        to the 'similar time periods
        """
        if diff <= threshold:
            similar_periods.append(current_period)

    return similar_periods

def get_temperature_input():
    while True:
        try:
            input_string = input("Enter 7 temperatures separated by commas: ")
            temperatures = [float(temp.strip()) for temp in input_string.split(",")]

            # Check if there is exactly 7 numbers input
            if len(temperatures) != 7:
                raise ValueError("Exactly 7 temperatures are required.")
            
            return temperatures
        # If you do not enter the correct input, Error output
        except ValueError as e:
            print("Invalid input. Please enter 7 numbers separated by commas. Error:", e)

# Load the merged file
file_path = 'merged_file.csv'  # Replace with the actual path to your file
merged_data = pd.read_csv(file_path)
tolerance = 5
# Prompt user for temperature input
input_temperatures = get_temperature_input()

# Find similar temperature periods
similar_periods = find_similar_temperature_periods(input_temperatures, merged_data, threshold=tolerance)

if similar_periods == []:
    print("We have found NO similar periods")

for index, period in enumerate(similar_periods):

    print(f"Similar period {index + 1}:\n", period, "\n")
    print("We have found", index + 1, "similar periods")