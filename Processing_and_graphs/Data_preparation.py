import pandas as pd
import os

# Path to the new working directory
#new_directory = "C:/Users/Sedláček/pr/Project-Weather-electricity-prices/Processing_and_graphs"
#new_directory = "c:/Users/jijia/OneDrive/Desktop/Project_ python/Project-Weather-electricity-prices/Processing_and_graphs"

# Changing the current working directory
#os.chdir(new_directory)

class Data_prep(object):
    
    def process_and_merge_weather_data(self, weather_base, weather_new):
        """
        Firstly, reading base excel file "Weather_base.xlsx" with weather data, renaming, dropping NAs, converting date into datetime object. 
        Secondly, reading "weather_new.csv" file, converting date column into proper datetime object, dropping out null values and final aggregation. 
        Finally, merging these two files into one Pandas DataFrame and saving as CSV file. 
        
        Parameters:
            weather_base (str): File path to the base weather data file.
            weather_new (str): File path to the new weather data file.

        Returns:
            None. It creates a csv file with three columns - date, temperature, value. 
        """
        # Read the 'Average temperature' sheet from the Excel file
        df = pd.read_excel(weather_base, sheet_name='Average temperature')

        # Drop the first three rows which contain metadata and headers
        df_transformed = df.drop([0, 1, 2])

        # Rename columns for clarity
        df_transformed.columns = ['Year', 'Month'] + list(range(1, 32))

        # Melt the dataframe to create two columns: one for dates, one for temperatures
        df_melted = df_transformed.melt(id_vars=['Year', 'Month'], value_vars=list(range(1, 32)), 
                                        var_name='Day', value_name='Temperature')

        # Drop rows with NaN temperatures
        df_melted = df_melted.dropna(subset=['Temperature'])

        # Convert year, month, and day columns to integers and then to a datetime object
        df_melted['Date'] = pd.to_datetime(df_melted[['Year', 'Month', 'Day']].astype(int))

        # Sorting by Date
        weather_base_done = df_melted[['Date', 'Temperature']].sort_values(by='Date')

        # Read the CSV file
        Weather_new = pd.read_csv(weather_new)
        Weather_new.columns = ['Date', 'Temperature']

        # Convert and format the 'Date' column
        Weather_new['Date'] = pd.to_datetime(Weather_new['Date'], format='%Y%m%dT%H%M')
        Weather_new['Date'] = Weather_new['Date'].dt.strftime('%Y-%m-%d')

        # Sort and reset index
        Weather_new = Weather_new.sort_values(by='Date')
        Weather_new = Weather_new.reset_index(drop=True)

        # Filter out null values and aggregate temperatures
        df_not_null_new = Weather_new[Weather_new['Temperature'].notna()]
        last_date_new = df_not_null_new['Date'].max()
        print("Our last available data are from:", last_date_new)

        Weather_new = Weather_new[Weather_new['Date'] <= last_date_new]
        Weather_new['Temperature'] = pd.to_numeric(Weather_new['Temperature'], errors='coerce')
        Weather_new = Weather_new.groupby('Date')['Temperature'].mean().reset_index()
        Weather_new.drop(index=0, inplace=True)
        Weather_new['Temperature'] = Weather_new['Temperature'].round(1)

        # Merge with base DataFrame
        merged_weather = pd.concat([weather_base_done, Weather_new], ignore_index=True)
        merged_weather.columns = ['Date', 'Temperature']

        # Convert and format the 'Date' column in merged DataFrame
        merged_weather['Date'] = pd.to_datetime(merged_weather['Date'])
        merged_weather['Date'] = merged_weather['Date'].dt.strftime('%Y-%m-%d')
        
        merged_weather.to_csv('Data/All_weather_data.csv', index = False, encoding='windows-1252')

    def merge_and_process_data(self, weather_data_path, value_data_path, output_file_path):
        """
        Merging two files "All_weather_data.csv" with "value.csv", removing duplicates, renaming columns and saving into csv format.

        Parameters:
        - weather_data_path (str): File path to the weather data file.
        - value_data_path (str): File path to the value data file.
        - output_file_path (str): File path to save the merged data.

        Returns:
        None. Creates a CSV file with three columns - date, temperature, value. 
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

#weather_base = "Weather_base.xlsx"
#weather_new = 'Weather_new.csv'

#weather_data_path = 'All_weather_data.csv'
#value_data_path = 'API_values.csv'
#output_file_path = "final_data.csv"

#Data_prep().process_and_merge_weather_data(weather_base, weather_new)


#Data_prep().merge_and_process_data(weather_data_path, value_data_path, output_file_path)
        
