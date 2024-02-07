## Searching for similar periods based of first difference

# Example input: 5, 6, 7, 8, 2, 4, 2, 7

import pandas as pd
import numpy as np

def searching_difference_diff(input_temperatures, final_data, threshold):
    """
    Function takes the data from input, computes the first difference of input values, 
    searches the dataset and finds time periods with similar temperature differences.
    You can adjust the threshold for setting the similarity, too.

    Parameters:
        input_temperatures - temperature values that user insert 
        final_data - the final data which includes weather values and also values downloaded from API 
        threshold - the level of similarity that user allows  
    
    Returns:
        Similar periods based on the inserted temperature values. 
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


