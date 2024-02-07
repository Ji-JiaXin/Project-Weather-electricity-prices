# Second try for finding similar values

# Searching for similar temperatures
import pandas as pd
import numpy as np
import os
# Path to the new working directory
#new_directory = "C:/Users/Sedláček/pr/Project-Weather-electricity-prices/Processing_and_graphs"
#new_directory = "c:/Users/jijia/OneDrive/Desktop/Project_ python/Project-Weather-electricity-prices/Processing_and_graphs"

# Change the current working directory
#os.chdir(new_directory)

#Verify the change
#print("New working directory:", os.getcwd())


def searching_difference_normal(input_temperatures, final_data, threshold):
    """
    Function takes the data from input, search whole dataset
      and find time periods with similar temperatures.
      You can adjust the threshold for setting the similarity, too.
    """
    if len(input_temperatures) != 7:
        raise ValueError("Input temperatures must be a list of 7 numbers.")

    data = pd.read_csv(final_data)

    #initializing an empty list for stucking the similar periods
    similar_periods = []

    # Iterating through the 'final_data' and checking 7-day periods
    for i in range(len(data) - 6):
        """ For each period, calculate the sum of square diff. between
            Temperatures and input Temperatures
           """
        current_period = data.iloc[i:i+7]
        current_temperatures = current_period['Temperature'].tolist()
        diff = sum((np.array(current_temperatures) - np.array(input_temperatures))**2)

        """ If the sum is less then 'treshold' then add the time period
        to the Similar time periods
        """
        if diff <= threshold:
            similar_periods.append(current_period)

    return similar_periods


# Load the merged file
#final_data = pd.read_csv('final_data.csv')

# Example usage
#input_temperatures, threshold = get_temperature_input()

# Find similar temperature periods
#similar_periods = searching_difference_normal(input_temperatures, final_data, threshold)
#print(similar_periods)

#if similar_periods == []:
    #print("We have found NO similar periods.You are to strict. Try to set higer threshold (8th number in the input).")

#for index, period in enumerate(similar_periods):
    #print(f"Similar period {index + 1}:\n", period, "\n")
    #print("We have found", index + 1, "similar periods")