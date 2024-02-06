# User Interface

# pip install customtkinter
import customtkinter
import tkinter
import pandas as pd
import sys

sys.path.append("C:/Users/Sedláček/pr/Project-Weather-electricity-prices")
#sys.path.append("c:/Users/jijia/OneDrive/Desktop/Project_ python/Project-Weather-electricity-prices/Processing_and_graphs")

from Processing_and_graphs.Searching_diff import searching_difference_diff
from Processing_and_graphs.Searching_normal import searching_difference_normal
from Processing_and_graphs.Data_preparation import Data_prep

from deutschland import smard
from deutschland.smard import Configuration
from deutschland.smard.api_client import ApiClient
from deutschland.smard.api_client import Endpoint as _Endpoint
from deutschland.smard.model.indices import Indices
from deutschland.smard.model.time_series import TimeSeries
from Processing_and_graphs.Electricity_API_download_data_latest import DownloadAPI

config = Configuration(host="https://www.smard.de/app", discard_unknown_keys=True)
api_client = ApiClient(config)
download_api = DownloadAPI(api_client)




customtkinter.set_ctk_parent_class(tkinter.Tk)

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# Choose your path
final_data = pd.read_csv('C:/Users/Sedláček/pr/Project-Weather-electricity-prices/Processing_and_graphs/final_data.csv')
#final_data = pd.read_csv('c:/Users/jijia/OneDrive/Desktop/Project_ python/Project-Weather-electricity-prices/Processing_and_graphs/final_data.csv')

weather_base = "Weather_base.xlsx"
weather_new = 'Weather_new.csv'

weather_data_path = 'All_weather_data.csv'
value_data_path = 'API_values.csv'
output_file_path = "final_data.csv"

input_row = []

import pandas as pd 

def retrieve_input():
    source = optionmenu_1.get()
    
    
    if source == "Generation off shore wind":
        energy_source = "Generation off shore wind"
    elif source == "Generation from other convential sources":
        energy_source = "Generation from other convential sources"
    elif source == "Generation from other renewables":
        energy_source = "Generation from other renewables"
    elif source == "Generation on shore wind":
        energy_source = "Generation on shore wind"
    elif source == "Generation from photovoltaics":
        energy_source = "Generation from photovoltaics"
    elif source == "Generation from pumper storage":
        energy_source = "Generation from pumper storage"
    elif source == "Total electricity consumption":
        energy_source = "Total electricity consumption"
    else:
        print("Invalid source selected.")
        return




    API_values = download_api.download_chart_data_by_name(filter_word= energy_source, filter_word_copy=energy_source, region="DE", region_copy="DE")
    API_values.to_csv('C:/Users/Sedláček/pr/Project-Weather-electricity-prices/Processing_and_graphs/API_values.csv', index = False, encoding='windows-1252')


    data_preparer = Data_prep()

    # Call the function
    data_preparer.process_and_merge_weather_data(weather_base, weather_new)


    data_preparer.merge_and_process_data(weather_data_path, value_data_path, output_file_path)
    
    input_row.clear()
    
    # Retrieve the method selected by the user
    method = combobox_1.get()

    try:
        input_temperatures = [
            float(entry_var_1.get()),
            float(entry_var_2.get()),
            float(entry_var_3.get()),
            float(entry_var_4.get()),
            float(entry_var_5.get()),
            float(entry_var_6.get()),
            float(entry_var_7.get()),
        ]
    except ValueError:
        print("Please enter valid numeric values for temperatures.")
        return

    try:
        threshold = float(entry_var_threshold.get())
    except ValueError:
        print("Please enter a valid numeric value for the threshold.")
        return

    # Call the appropriate function based on the selected method
    if method == "Normal":
        similar_periods = searching_difference_normal(input_temperatures, final_data, threshold)
    elif method == "Differentiated":
        similar_periods = searching_difference_diff(input_temperatures, final_data, threshold)
    else:
        print("Invalid method selected.")
        return

    for index, period in enumerate(similar_periods):
        print(f"Similar period {index + 1}:\n", period, "\n")
    
    print('We have found', len(similar_periods), 'similar periods')




root = customtkinter.CTk()
root.geometry("400x680")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text = "Please insert seven temperature values in Celsius and the threshold value")
label.pack(pady=20, padx=20)

entry_var_1 = tkinter.StringVar()
entry_var_2 = tkinter.StringVar()
entry_var_3 = tkinter.StringVar()
entry_var_4 = tkinter.StringVar()
entry_var_5 = tkinter.StringVar()
entry_var_6 = tkinter.StringVar()
entry_var_7 = tkinter.StringVar()
entry_var_threshold = tkinter.StringVar()

entry_1 = customtkinter.CTkEntry(master=frame, textvariable= entry_var_1)
entry_1.pack(pady=10, padx=10)

entry_2 = customtkinter.CTkEntry(master=frame, textvariable= entry_var_2)
entry_2.pack(pady=10, padx=10)

entry_3 = customtkinter.CTkEntry(master=frame, textvariable= entry_var_3)
entry_3.pack(pady=10, padx=10)

entry_4 = customtkinter.CTkEntry(master=frame, textvariable= entry_var_4)
entry_4.pack(pady=10, padx=10)

entry_5 = customtkinter.CTkEntry(master=frame, textvariable= entry_var_5)
entry_5.pack(pady=10, padx=10)

entry_6 = customtkinter.CTkEntry(master=frame, textvariable= entry_var_6)
entry_6.pack(pady=10, padx=10)

entry_7 = customtkinter.CTkEntry(master=frame, textvariable= entry_var_7)
entry_7.pack(pady=10, padx=10)

entry_threshold = customtkinter.CTkEntry(master=frame, textvariable= entry_var_threshold)
entry_threshold.pack(pady=10, padx=10)


optionmenu_1 = customtkinter.CTkOptionMenu(frame, values=["Generation off shore wind", 
            "Generation from other convential sources", "Generation from other renewables",
            "Generation on shore wind", "Generation from photovoltaics",
            "Generation from pumper storage", "Total electricity consumption"])
optionmenu_1.pack(pady=10, padx=10)
optionmenu_1.set("Source")

combobox_1 = customtkinter.CTkComboBox(frame, values=["Normal", "Differentiated"])
combobox_1.pack(pady=10, padx=10)
combobox_1.set("Method")

button = customtkinter.CTkButton(master = frame, text = "Find", command= retrieve_input)
button.pack(pady=12,padx=10)

root.mainloop()
 