#importing necessary packages
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates

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
    graph_creator_one_period(similar_periods):
        Creating a graph covering the whole time period of the data. Uses the "final_data.csv", creates a plot describing the envolvement of temperature and values over time.
        It also highlights dates with similar weather pattern. 
    
    graph_creator_year(similar_periods):
        Creating a series of subplots in a 3x4 grid, each representing a certain year. Similarly to previous method, it plots the temperature and values over time and highlights dates with similar patterns. 
    """
    def graph_creator_one_period(similar_periods):
        """
        Loading of the final_data.csv, plotting of two variables over time (temperature, values). 
        Highlighting the dates with similar weather patterns (the output from searching_first_diff.py or searching_sqr_diff.py).
        
        Parameters:
            similar_periods - A set of dates from searching_first_diff.py or searching_sqr_diff.py
        
        Returns:
        A plot displaying the relationship between temperature and the downloaded data from API with highlighted days.  
        """
        # Loading the merged file
        file_path = 'Data/final_data.csv'
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
        for period in similar_periods:
            for day in period['Date']:
                axes_temperature.axvline(pd.to_datetime(day), color='red', linestyle=':', linewidth=2, zorder=2)

        # Adding a legend and title 
        fig.tight_layout()
        #fig.legend(loc='upper left', bbox_to_anchor=(0.6,0.95))
        plt.title('Relationship between Temperature and Values')

        # Displaying the plot
        plt.savefig(f'whole_period.png')
        plt.show()

    
    

    def graph_creator_year(similar_periods):
        """
        Loading of the final_data.csv and creating subplots only for the years where similar_periods are found.
        Each set of graphs will be saved as a separate image only if similar_periods are present in that year.
        
        Parameters:
            similar_periods - A set of dates from searching_first_diff.py or searching_sqr_diff.py
        
        Returns:
        Subplots displaying the relationship between temperature and the downloaded data from API with highlighted days.  
        """
        # Loading the merged file
        file_path = 'Data/final_data.csv'
        df = pd.read_csv(file_path)

        # Making sure that the Date variable is in Datetime format
        df['Date'] = pd.to_datetime(df['Date'])

        # Get years from our data frame
        years = df['Date'].dt.year.unique()

        for year in years:
            # Check if there are similar periods in this year
            if any(pd.to_datetime(similar_period['Date']).dt.year.eq(year).any() for similar_period in similar_periods):
                fig, ax = plt.subplots(figsize=(10, 5))
                
                # Plotting the values downloaded from API
                df_year = df[df['Date'].dt.year == year]
                ax.plot(df_year['Date'], df_year['Values'], label=f'Year {year}', color='darkblue')
                ax.set_title(f'Year {year}')
                ax.set_xticks([])
                ax.set_ylabel('Values', color='darkblue', fontsize=8)

                # Format the dates on the x-axis
                ax.xaxis_date()  
                ax.xaxis.set_major_locator(mdates.MonthLocator())  
                ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))  
                ax.xaxis.set_minor_locator(mdates.DayLocator())  
                fig.autofmt_xdate()  

                # Adding temperature variable
                ax_temp = ax.twinx()
                ax_temp.plot(df_year['Date'], df_year['Temperature'], label='Temperature', color='green')
                ax_temp.set_ylabel('Temperature', color='green', fontsize=8)

                # Setting tick parameters
                ax.tick_params(axis='x', labelsize=6)
                ax.tick_params(axis='y', labelsize=6)
                ax_temp.tick_params(axis='y', labelsize=6)

                # Highlighting similar periods
                for similar_period_df in similar_periods:
                    similar_period_df['Date'] = similar_period_df['Date'].apply(
                        lambda x: x.strftime('%Y-%m-%d') if isinstance(x, datetime.datetime) else x
                    )
                    for day in similar_period_df['Date']:
                        if day in df_year['Date'].astype(str).values:
                            ax.axvline(pd.to_datetime(day), color='red', linestyle=':', linewidth=1)

                # Adjust layout for each figure and save
                plt.tight_layout()
                plt.savefig(f'year_graph_{year}.png')
                plt.show()
