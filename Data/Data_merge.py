import pandas as pd


def merge_and_process_data(weather_data_path, value_data_path, output_file_path):
    """
    Merging two files "All_weather_data.csv" with "value.csv", removing duplicates, renaming columns and saving into csv format.
    Returns:
    CSV file with three columns - date, temperature, value. 
    """
    # Loading the files
    data_1 = pd.read_csv(weather_data_path)
    data_2 = pd.read_csv(value_data_path)

    # Merge the files on the 'Date' column
    merged_data = pd.merge(data_1, data_2, on='Date', how='inner')

    # Remove duplicate rows and group by the 'Date' column, averaging the values
    merged_data = merged_data.drop_duplicates()
    merged_data = merged_data.groupby('Date', as_index=False).mean()
    merged_data['Temperature'] = merged_data['Temperature'].round(1)
    
    # Checking the data
    print(merged_data)
    
    # Saving the merged data to a new file
    merged_data.to_csv(output_file_path, index=False)
