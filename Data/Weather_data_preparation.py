# Takhle je to all right
import pandas as pd

def process_and_merge_weather_data(weather_base, weather_new):
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
    

    merged_weather.to_csv('All_weather_data.csv', index = False, encoding='windows-1252')
