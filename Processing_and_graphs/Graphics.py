#importing necessary packages
import os
import pandas as pd
import matplotlib.pyplot as plt

# Path to the new working directory
#new_directory = "C:/Users/Sedláček/pr/Project-Weather-electricity-prices/Data"
new_directory = "C:/Users/jijia/OneDrive/Desktop/Project_ python/Project-Weather-electricity-prices/Data"

# Changing the current working directory
os.chdir(new_directory)


# Graph
class Visualisator(object):
    """
    The class includes functions for visualisation of the relationship between the values and temperature taken from the "final_data.csv". 
    ....
    Attributes
    ----------
    None
    ....

    Methods
    ----------
    graph_creator_one_period(output_dates):
        Creating a graph covering the whole time period of the data. Uses the "final_data.csv", creates a plot describing the envolvement of temperature and values over time.
        It also highlights dates with similar weather pattern. 
    
    graph_creator_year(output_dates):
        Creating a series of subplots in a 3x4 grid, each representing a certain year. Similarly to previous method, it plots the temperature and values over time and highlights dates with similar patterns. 
    """
    def graph_creator_one_period(output_dates):
        """
        Loading of the final_data.csv, plotting of two variables over time (temperature, values). 
        Highlighting the dates with similar weather patterns (the output from searching_first_diff.py or searching_sqr_diff.py).
        
        Parameters:
            output_dates - A set of dates from searching_first_diff.py or searching_sqr_diff.py
        
        Returns:
        A plot displaying the relationship between temperature and the downloaded data from API with highlighted days.  
        """
        # Loading the merged file
        file_path = 'final_data.csv'
        df = pd.read_csv(file_path)
        
        #making sure that the Date variable is in Datetime format
        df['Date'] = pd.to_datetime(df['Date'])

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
        for day in output_dates:
            axes_temperature.axvline(pd.to_datetime(day), color='red', linestyle=':', linewidth=2, zorder=2)

        # Adding a legend and title 
        fig.tight_layout()
        fig.legend(loc='upper left', bbox_to_anchor=(0.6,0.95))
        plt.title('Relationship between Temperature and Values')

        # Displaying the plot
        plt.show()

    def graph_creator_year(output_dates):
        """
        Loading of the final_data.csv, creating subplots into a grid 3x4 with a use of for loop. 
        Highlighting the dates with similar weather patterns (the output from searching_first_diff.py or searching_sqr_diff.py).
    
        Parameters:
            output_dates - A set of dates from searching_first_diff.py or searching_sqr_diff.py
        
        Returns:
        Subplots displaying the relationship between temperature and the downloaded data from API with highlighted days.  
        """
        # Loading the merged file
        file_path = 'final_data.csv'
        df = pd.read_csv(file_path)

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

        # printing the plot
        plt.show()


#the days we got from our code for searching of similar weather patterns  
#example
output_dates = {'2015-02-11', '2015-02-12','2015-02-13','2015-02-14','2015-02-15','2015-02-16','2015-02-17','2015-02-18','2015-02-19',
                    '2016-02-11', '2016-02-12','2016-02-13','2016-02-14','2016-02-15','2016-02-16','2016-02-17','2016-02-18','2023-02-19'}

Visualisator.graph_creator_year(output_dates)
#Visualisator.graph_creator_one_period(output_dates)