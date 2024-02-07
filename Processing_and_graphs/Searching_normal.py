# Second try for finding similar values

# Searching for similar temperatures
import pandas as pd
import numpy as np

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
