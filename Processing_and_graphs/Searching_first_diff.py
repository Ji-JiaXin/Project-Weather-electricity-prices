## Searching for similar periods based of first difference

# Example input: 5, 6, 7, 8, 2, 4, 2, 7

import pandas as pd
import os
import numpy as np

# preparign the data
# Path to the new working directory
new_directory = "C:/Users/Sedláček/pr/Project-Weather-electricity-prices/Processing_and_graphs"
#new_directory = "c:/Users/jijia/OneDrive/Desktop/Project_ python/Project-Weather-electricity-prices/Processing_and_graphs"

# Change the current working directory
os.chdir(new_directory)

# Verify the change
print("New working directory:", os.getcwd())


def searching_difference(input_temperatures, data, threshold):
    """
    Function takes the data from input, computes the first difference of input values, 
    searches the dataset and finds time periods with similar temperature differences.
    You can adjust the threshold for setting the similarity, too.
    """
    if len(input_temperatures) != 7:
        # Pactically not necessary, just to be sure
        raise ValueError("Input temperatures must be a list of 7 numbers.")

    # Usinf Numpy to compute the first difference of the input temperatures
    input_diff = np.diff(input_temperatures)

    # Initializing an empty list for stacking the similar periods
    similar_periods = []

    # Adding a Temperature_Diff column to the merged_data
    merged_data['Temperature_Diff'] = merged_data['Temperature'].diff().fillna(0)
    
    # Iterating through the 'Data' and checking 6-day periods (since we're comparing differences)
    for i in range(len(data) - 5):
        # For each period, calculate the sum of squared differences between
        # the Temperature_Diff and input temperature differences
        current_period = data.iloc[i:i+6]
        current_diffs = current_period['Temperature_Diff'].tolist()
        diff = sum((np.array(current_diffs) - np.array(input_diff))**2)

        # If the sum is less than 'threshold', then add the time period to the similar time periods
        if diff <= threshold:
            similar_periods.append(current_period)

    return similar_periods


def get_temperature_input():
    """
    Function created for collecting the input.
    Taking first 7 numbers as temperature values and the last 8th as the threshold.
    """
    while True:
        try:
            # Prompting for 7 temperatures and an additional number for the threshold
            input_string = input("Enter 7 temperatures followed by a threshold, all separated by commas: ")
            input_numbers = [float(num.strip()) for num in input_string.split(",")]

            # Checking if there are exactly 8 numbers (7 temperatures + 1 threshold)
            if len(input_numbers) != 8:
                raise ValueError("Exactly 7 temperatures and 1 threshold are required.")

            # Separating the temperatures and the threshold
            temperatures = input_numbers[:7]
            threshold = input_numbers[7]

            return temperatures, threshold
        except ValueError as e:
            # Handling invalid input
            print("Invalid input. Please enter 7 temperatures and 1 threshold, all separated by commas. Error:", e)

# Loading the merged file
merged_data = pd.read_csv('final_data.csv')

# Setting the values of the variables
input_temperatures, threshold = get_temperature_input()

# Find similar temperature difference periods
similar_periods = searching_difference(input_temperatures, merged_data, threshold)

if similar_periods == []:
    print("We have found NO similar periods. You are too strict. Try to set a higher threshold (8th number in the input).")

for index, period in enumerate(similar_periods):
    print(f"Similar period {index + 1}:\n", period, "\n")
    print('We have found',len(similar_periods),'similar periods')


