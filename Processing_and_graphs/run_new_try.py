from User_interface import retrieve_input
from Electricity_API_download_data_latest import DownloadAPI
from Data_preparation import Data_prep
import Searching_first_diff
import Searching_sqr_diff
from Graphics import Visualisator


# Main execution function that calls the others - 
def main_runner():
    input_values = retrieve_input()
    if input_values:
        temperatures, threshold, source_energy, method_selected = input_values
        filter_word = source_energy
        filter_word_copy = source_energy
        region = "DE"

        # Downloading data using API
        download_api = DownloadAPI()
        downloaded_data = download_api.download_chart_data_by_name(
            filter_word, filter_word_copy, region, region, timestamp=None, resolution="day"
        )

        # Data preparation - merging downloaded data with available weather data -> creating our final_data.csv

        # Finding similar weather patterns - using either Searching_first_diff.py or Searching_sqr_diff.py

        # Visualisation of the output -> creating a plot with highted days when the weather pattern was similar 


# Executing main function
if __name__ == "__main__":
    main_runner()
