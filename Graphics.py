#importing necessary packages
import pandas as pd
import matplotlib.pyplot as plt

# Loading the merged file
file_path = 'merged_file.csv'
df = pd.read_csv(file_path)

#print(df)

#making sure that the Date variable is in Datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Graph

# Plot the temperature
fig, axes_temperature = plt.subplots()
color_outline= 'black'
axes_temperature.set_xlabel('Date', color=color_outline)
axes_temperature.set_ylabel('Temperature', color=color_outline)
axes_temperature.plot(df['Date'], df['Temperature'], color='lightblue',zorder=1)
axes_temperature.tick_params(axis='y', labelcolor=color_outline)

# Plot the values
axes_values = axes_temperature.twinx()
axes_values.set_ylabel('Values', color=color_outline)
axes_values.plot(df['Date'], df['Values'], color='lightgreen',zorder=1)
axes_values.tick_params(axis='y', labelcolor=color_outline)

#highlight the output days from the function processing similar weather patterns 
chosen_dates = ['2015-02-11', '2015-02-12','2015-02-13','2015-02-14','2015-02-15','2015-02-16','2015-02-17','2015-02-18','2015-02-19']

axes_temperature.scatter(df[df['Date'].isin(chosen_dates)]['Date'], df[df['Date'].isin(chosen_dates)]['Temperature'], 
                    color='orange', label='Dates with similar weather pattern', marker='*',zorder=3)
axes_values.scatter(df[df['Date'].isin(chosen_dates)]['Date'], df[df['Date'].isin(chosen_dates)]['Values'], 
                    color='orange', marker='o',zorder=3)

# Adding a legend
fig.tight_layout()
fig.legend(loc='upper left', bbox_to_anchor=(0.6,0.95))
plt.title('Relationship between Temperature and Values')

# Displaying the plot
plt.show()

#

