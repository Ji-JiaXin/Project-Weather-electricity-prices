#importing necessary packages
import os
import pandas as pd
import matplotlib.pyplot as plt

# Path to the new working directory
new_directory = "C:/Users/Sedláček/pr/Project-Weather-electricity-prices/Data"

# Changing the current working directory
os.chdir(new_directory)

# Loading the merged file
file_path = 'merged_data.csv'
df = pd.read_csv(file_path)

#the days we got from our code for searching of similar weather patterns  
    #example
chosen_dates = {'2015-02-11', '2015-02-12','2015-02-13','2015-02-14','2015-02-15','2015-02-16','2015-02-17','2015-02-18','2015-02-19',
                    '2016-02-11', '2016-02-12','2016-02-13','2016-02-14','2016-02-15','2016-02-16','2016-02-17','2016-02-18','2023-02-19'}

#making sure that the Date variable is in Datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Graph

# Plot the temperature
fig, axes_temperature = plt.subplots()
color_outline= 'black'
axes_temperature.set_xlabel('Date', color=color_outline)
axes_temperature.set_ylabel('Temperature', color=color_outline)
axes_temperature.plot(df['Date'], df['Temperature'], color='darkblue', linewidth=0.4,zorder=1)
axes_temperature.tick_params(axis='y', labelcolor=color_outline)

# Plot the values
axes_values = axes_temperature.twinx()
axes_values.set_ylabel('Values', color=color_outline)
axes_values.plot(df['Date'], df['Values'], color='darkgreen',linewidth=0.4,zorder=1)
axes_values.tick_params(axis='y', labelcolor=color_outline)

#highlight the output days from the function searching for similar weather patterns by - adding dotted lines
for day in chosen_dates:
    axes_temperature.axvline(pd.to_datetime(day), color='red', linestyle=':', linewidth=2, zorder=2)

# Adding a legend and title 
fig.tight_layout()
fig.legend(loc='upper left', bbox_to_anchor=(0.6,0.95))
plt.title('Relationship between Temperature and Values')

# Displaying the plot
plt.show()


