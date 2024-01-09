import pandas as pd

def process_csv(input_file_path, output_file_path):
    # Read the CSV file
    df = pd.read_csv(input_file_path, sep=';')

    # Define the columns to include
    columns_to_include = [
        'Date', 'Total (grid load) [MWh] Calculated resolutions',
        'Residual load [MWh] Calculated resolutions',
        'Hydro pumped storage [MWh] Calculated resolutions'
    ]

    # Select the columns for the new DataFrame
    new_df = df[columns_to_include]

    # Define the new column names
    rename_dict = {
        'Total (grid load) [MWh] Calculated resolutions': 'Tot_cons',
        'Residual load [MWh] Calculated resolutions': 'Res_load',
        'Hydro pumped storage [MWh] Calculated resolutions': 'Hydro_pumped'
    }

    # Rename the columns
    new_df.rename(columns=rename_dict, inplace=True)

    # Save the processed DataFrame to a new CSV file
    new_df.to_csv(output_file_path, sep=';', index=True)

    return new_df

# Example usage of the function
input_path = 'C:/Users/Sedláček/OneDrive - FSV/Documents/DataProcessingPython/Project-Weather-electricity-prices/Consumption.csv'
output_path = 'new_file.csv'
processed_df = process_csv(input_path, output_path)