##  Weather preparation
import os
import pandas as pd

# Path to the new working directory
new_directory = "C:/Users/Sedláček/pr/Project-Weather-electricity-prices"

# Changing the current working directory
os.chdir(new_directory)

# Verifing the change
print("New working directory:", os.getcwd())

# Path to my Excel file. (If the souse file is not in Excel format, need to adjust the next command)
file_path = 'Weather_base.xlsx'  

# Read the 'Average temperature' sheet from file containing data about weather.
# If the data sourse is not in Excel format, need to use 'pd.read_csv() or different way'
df = pd.read_excel(file_path, sheet_name='Average temperature')

# Drop the first three rows which contain metadata and headers
df_transformed = df.drop([0, 1, 2])

# Rename columns for clarity
df_transformed.columns = ['Year', 'Month'] + list(range(1, 32))

# Melt the dataframe to create two columns: one for dates, one for temperatures
# Nedd to transform data to standartize frame
df_melted = df_transformed.melt(id_vars=['Year', 'Month'], value_vars=list(range(1, 32)), 
                                var_name='Day', value_name='Temperature')

# Drop rows with NaN temperatures
df_melted = df_melted.dropna(subset=['Temperature'])

# Convert year, month, and day columns to integers and then to a datetime object
df_melted['Date'] = pd.to_datetime(df_melted[['Year', 'Month', 'Day']].astype(int))

# Select and order the final columns
Weather_base = df_melted[['Date', 'Temperature']].sort_values(by='Date')

# Display the first few rows of the transformed dataframe








Weather_new = pd.read_csv('Weather_new.csv')
Weather_new = Weather_new.iloc[10:]
Weather_new.columns = ['Date', 'Temperature']
# Convert the 'Date' column to datetime format
Weather_new['Date'] = pd.to_datetime(Weather_new['Date'], format='%Y%m%dT%H%M')
# Format the datetime objects to the desired date format
Weather_new['Date'] = Weather_new['Date'].dt.strftime('%Y-%m-%d')




Weather_new = Weather_new.sort_values(by='Date')
Weather_new = Weather_new.reset_index(drop=True)



Weather_base = Weather_base.sort_values(by='Date')
Weather_base = Weather_base.reset_index(drop=True)



# Filtering out rows where 'values' is not Null or NaN/NA
df_not_null_new = Weather_new[Weather_new['Temperature'].notna()]
df_not_null_base = Weather_base[Weather_base['Temperature'].notna()]


# Finding the last date with a non-null or non-NA/Nan value
last_date_new = df_not_null_new['Date'].max()

#print(Weather_base)
#print("Our last avaivable data are form:", last_date_new)

# Erasing rows for which we don't have a value Value
Weather_new = Weather_new[Weather_new['Date'] <= last_date_new]

Weather_new['Temperature'] = pd.to_numeric(Weather_new['Temperature'], errors='coerce')

# Group by 'Date' and calculate the mean of 'Temperature' for each group
Weather_new = Weather_new.groupby('Date')['Temperature'].mean()

# Reset the index to get a DataFrame instead of a Series
Weather_new = Weather_new.reset_index()
Weather_new.drop(index = 0, inplace = True)
Weather_new['Temperature'] = Weather_new['Temperature'].round(1)


#print(Weather_new)

merged_weather = pd.concat([Weather_base, Weather_new], ignore_index=True)
merged_weather.columns = ['Date', 'Temperature']

merged_weather['Date'] = pd.to_datetime(merged_weather['Date'])
# Format the datetime objects to 'YYYY-MM-DD' string format
merged_weather['Date'] = merged_weather['Date'].dt.strftime('%Y-%m-%d')

print(merged_weather)

merged_weather.to_csv('Weather_data', index = False, encoding='windows-1252')