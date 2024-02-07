## Searching for similar periods based of first difference

# Example input: 5, 6, 7, 8, 2, 4, 2, 7

import pandas as pd
import os
import numpy as np

# preparign the data
# Path to the new working directory
#new_directory = "C:/Users/Sedláček/pr/Project-Weather-electricity-prices/Processing_and_graphs"
#new_directory = "c:/Users/jijia/OneDrive/Desktop/Project_ python/Project-Weather-electricity-prices/Processing_and_graphs"

# Change the current working directory
#os.chdir(new_directory)

# Verify the change 
#print("New working directory:", os.getcwd())


def searching_difference_diff(input_temperatures, final_data, threshold):
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
    
    data = pd.read_csv(final_data)
    # Adding a Temperature_Diff column to the merged_data
    data['Temperature_Diff'] = data['Temperature'].diff().fillna(0)
    
    # Initializing an empty list for stacking the similar periods
    similar_periods = []

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

# Loading the merged file
#data = pd.read_csv('final_data.csv')

# Setting the values of the variables
#input_temperatures, threshold = get_temperature_input()

# Find similar temperature difference periods
#similar_periods = searching_difference_diff(input_temperatures, final_data, threshold)

#if similar_periods == []:
    #print("We have found NO similar periods. You are too strict. Try to set a higher threshold (8th number in the input).")

#for index, period in enumerate(similar_periods):
    #print(f"Similar period {index + 1}:\n", period, "\n")
    #print('We have found',len(similar_periods),'similar periods')


