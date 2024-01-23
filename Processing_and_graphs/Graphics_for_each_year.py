#importing necessary packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Loading the merged file
file_path = 'merged_file.csv'
df = pd.read_csv(file_path)
#print(df)

#the days we got from our code for searching of similar weather patterns  
    #just an example
output_dates = {'2015-02-11', '2015-02-12','2015-02-13','2015-02-14','2015-02-15','2015-02-16','2015-02-17','2015-02-18','2015-02-19',
                    '2016-02-11', '2016-02-12','2016-02-13','2016-02-14','2016-02-15','2016-02-16','2016-02-17','2016-02-18','2023-02-19'}

# Making sure that the Date variable is in Datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Get years from our data frame
years = df['Date'].dt.year.unique()

# Create smaller plots for each year - we create a grid 3x4
fig, axes_years= plt.subplots(nrows=3, ncols=4, figsize=(9, 9), sharey=True)

# Plot each year separately
axes_years = axes_years.flatten()
# Using for loop to iterate 
for n, year in enumerate(years):
    # plotting the values downloaded from API 
    df_year = df[df['Date'].dt.year == year]
    axes_years[n].plot(df_year['Date'], df_year['Values'], label=f'Year {year}',color='darkblue')
    axes_years[n].set_title(f'Year {year}')
    axes_years[n].set_xticks([])
    axes_years[n].set_ylabel('Values',color='darkblue',fontsize=5)

    # adding temperature variable 
    axes_temp = axes_years[n].twinx()
    axes_temp.plot(df_year['Date'], df_year['Temperature'], label='Temperature', color='green')
    axes_temp.set_ylabel('Temperature', color='green',fontsize=5)

    # setting tick parameters 
    axes_years[n].tick_params(axis='x', labelsize=5)
    axes_years[n].tick_params(axis='y', labelsize=5)
    axes_temp.tick_params(axis='y', labelsize=5)

    # highlight specific dates 
    #iterating trough the dataset searching if the date is there and then putting a dotted line in the graph
    for day in output_dates:
        if day in df_year['Date'].astype(str).values:
            axes_years[n].axvline(pd.to_datetime(day), color='red', linestyle=':', linewidth=1)

# Final touches - adjusting layout and title 
fig.tight_layout()
#fig.legend(loc='upper left', bbox_to_anchor=(0.6,0.95))
#plt.title('Relationship between Temperature and Values')

# printing the plot
plt.show()
