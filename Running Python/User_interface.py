# User Interface - the runner of our whole project

# Example first input:
   # "C:/Users/Sedláček/pr/Project-Weather-electricity-prices"

# pip install customtkinter
import customtkinter
import tkinter
import pandas as pd
import sys
import os
import tkinter.font as tkFont

# to process inserted path - get rid off the wrong backslash
def on_set():
    global directory_path
    directory_path = entry.get().strip('\"')
    app.destroy()

# Setting the theme and scaling before creating the main window
customtkinter.set_appearance_mode("dark")  # Other options: "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Other options like "dark-blue", "green"
app = customtkinter.CTk()
app.geometry('400x300')
app.title("Set Working Directory")

# Main text for the first GUI
label_text = """Please enter your working directory,
where you have downloaded our GitHub repository.
Then press the Set buttom and the working directory
will be set for further usage."""
font_style_label = customtkinter.CTkFont(family="Times New Roman", size=15)
label = customtkinter.CTkLabel(app, text=label_text, font=font_style_label)
label.pack(pady=10)

entry = customtkinter.CTkEntry(app)
entry.pack(pady=10)
set_button = customtkinter.CTkButton(app, text="Set", command=on_set)
set_button.pack(pady=10)
app.mainloop()

if directory_path:  # Check if directory_path was set
    sys.path.append(directory_path)
    print(f"Directory path {directory_path} added to sys.path")
else:
    print("No directory path was set.")

new_directory = directory_path

# Changing the current working directory
os.chdir(new_directory)

# importing needed modules from other files
from Processing_and_graphs.Searching_diff import searching_difference_diff
from Processing_and_graphs.Searching_normal import searching_difference_normal
from Processing_and_graphs.Data_preparation import Data_prep
from Processing_and_graphs.Electricity_API_download_data_latest import DownloadAPI
from Processing_and_graphs.Graphics import Visualisator

from deutschland import smard
from deutschland.smard import Configuration
from deutschland.smard.api_client import ApiClient
from deutschland.smard.api_client import Endpoint as _Endpoint
from deutschland.smard.model.indices import Indices
from deutschland.smard.model.time_series import TimeSeries

config = Configuration(host="https://www.smard.de/app", discard_unknown_keys=True)
api_client = ApiClient(config)
download_api = DownloadAPI(api_client)

#GUI
customtkinter.set_ctk_parent_class(tkinter.Tk)

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# Don't touch, setting default
final_data = 'Data/final_data.csv'
weather_new = 'Data/Weather_new.csv'
weather_base = 'Data/Weather_base.xlsx'

weather_data_path = 'Data/All_weather_data.csv'
value_data_path = 'Data/API_values.csv'
output_file_path = 'Data/final_data.csv'

input_row = []

# the main running fuction
def retrieve_input():
    source = optionmenu_1.get()

    ##1.step - Based on the user selected source, we download the data from API 
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
    #downloading the data 
    API_values = download_api.download_chart_data_by_name(filter_word= energy_source, filter_word_copy=energy_source, region="DE", region_copy="DE")
    API_values.to_csv('Data/API_values.csv', index = False, encoding='windows-1252')
    #API_values.to_csv('c:/Users/jijia/OneDrive/Desktop/Project_ python/Project-Weather-electricity-prices/Processing_and_graphs/API_values', index = False, encoding='windows-1252')

    ##2.step - preparing and merging weather data 
    data_preparer = Data_prep()
    # Call the function
    data_preparer.process_and_merge_weather_data(weather_base, weather_new)
    data_preparer.merge_and_process_data(weather_data_path, value_data_path, output_file_path)
    input_row.clear()

    ##3.step - getting the chosen method from user, some input validation (temperature must be numeric, exactly 7 values + 1 threshold) 
    # Retrieve the method selected by the user
    method = combobox_1.get()
    # input validation
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
    
    ##4. Creating graphs
    graph_choice = combobox_2.get()
    # Call the appropriate function based on the selected method
    if graph_choice == "For each year":
        Visualisator.graph_creator_year(similar_periods)
    elif graph_choice == "Whole period":
        Visualisator.graph_creator_one_period(similar_periods)
    else:
        print("Invalid type of graph selected.")
        return
    root.destroy()


# Adjusting the graphical part of GUI
root = customtkinter.CTk()
root.geometry("700x780")
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=5, padx=60, fill="both", expand=True)
font_style_head= customtkinter.CTkFont(family="Times New Roman", size=14, weight="bold")
font_style = customtkinter.CTkFont(family="Times New Roman", size=9)

#Setting the entry bubbles
entry_var_1 = tkinter.StringVar()
entry_var_2 = tkinter.StringVar()
entry_var_3 = tkinter.StringVar()
entry_var_4 = tkinter.StringVar()
entry_var_5 = tkinter.StringVar()
entry_var_6 = tkinter.StringVar()
entry_var_7 = tkinter.StringVar()
entry_var_threshold = tkinter.StringVar()

# For the 1st temperature value 
label_1 = customtkinter.CTkLabel(master=frame, text = "Please insert seven temperature values in Celsius and the threshold value")
label_1.pack(pady=5, padx=5)
label_1.configure(font=font_style_head)
label_entry_1 = customtkinter.CTkLabel(master=frame, text="1st temperature (°C):")
label_entry_1.pack(pady=(0,0), padx=5)
label_entry_1.configure(font=font_style)
entry_1 = customtkinter.CTkEntry(master=frame, textvariable= entry_var_1)
entry_1.pack(pady=0.5, padx=5)
entry_1.configure(font=font_style)

# For the 2nd temperature value 
label_entry_2 = customtkinter.CTkLabel(master=frame, text="2nd temperature (°C):")
label_entry_2.pack(pady=(0,0), padx=5)
label_entry_2.configure(font=font_style)
entry_2 = customtkinter.CTkEntry(master=frame, textvariable= entry_var_2)
entry_2.pack(pady=0.5, padx=5)
entry_2.configure(font=font_style)

# For the 3rd temperature value 
label_entry_3 = customtkinter.CTkLabel(master=frame, text="3rd temperature (°C):")
label_entry_3.pack(pady=(0,0), padx=5)
label_entry_3.configure(font=font_style)
entry_3 = customtkinter.CTkEntry(master=frame, textvariable= entry_var_3)
entry_3.pack(pady=0.5, padx=5)
entry_3.configure(font=font_style)

# For the 4th temperature value 
label_entry_4 = customtkinter.CTkLabel(master=frame, text="4st temperature (°C):")
label_entry_4.pack(pady=(0,0), padx=5)
label_entry_4.configure(font=font_style)
entry_4 = customtkinter.CTkEntry(master=frame, textvariable= entry_var_4)
entry_4.pack(pady=0.5, padx=5)
entry_4.configure(font=font_style)

# For the 5th temperature value 
label_entry_5 = customtkinter.CTkLabel(master=frame, text="5st temperature (°C):")
label_entry_5.pack(pady=(0,0), padx=5)
label_entry_5.configure(font=font_style)
entry_5 = customtkinter.CTkEntry(master=frame, textvariable= entry_var_5)
entry_5.pack(pady=0.5, padx=5)
entry_5.configure(font=font_style)

# For the 6th temperature value 
label_entry_6 = customtkinter.CTkLabel(master=frame, text="6st temperature (°C):")
label_entry_6.pack(pady=(0,0), padx=5)
label_entry_6.configure(font=font_style)
entry_6 = customtkinter.CTkEntry(master=frame, textvariable= entry_var_6)
entry_6.pack(pady=0.5, padx=5)
entry_6.configure(font=font_style)

# For the 7th temperature value 
label_entry_7 = customtkinter.CTkLabel(master=frame, text="7st temperature (°C):")
label_entry_7.pack(pady=(0,0), padx=5)
label_entry_7.configure(font=font_style)
entry_7 = customtkinter.CTkEntry(master=frame, textvariable= entry_var_7)
entry_7.pack(pady=0.5, padx=5)
entry_7.configure(font=font_style)

# For the threshold 
label_entry_thre = customtkinter.CTkLabel(master=frame, text="Threshold (integer between 5-10):")
label_entry_thre.pack(pady=(0,0), padx=5)
label_entry_thre.configure(font=font_style)
entry_threshold = customtkinter.CTkEntry(master=frame, textvariable= entry_var_threshold)
entry_threshold.pack(pady=0.5, padx=5)
entry_threshold.configure(font=font_style)

# For the list of possible sources that user can choose from
optionmenu_1 = customtkinter.CTkOptionMenu(frame, values=["Generation off shore wind", 
            "Generation from other convential sources", "Generation from other renewables",
            "Generation on shore wind", "Generation from photovoltaics",
            "Generation from pumper storage", "Total electricity consumption"])
optionmenu_1.pack(pady=5, padx=5)
optionmenu_1.set("Source")
optionmenu_1.configure(font=font_style)

# For the methods
combobox_1 = customtkinter.CTkComboBox(frame, values=["Normal", "Differentiated"])
combobox_1.pack(pady=5, padx=5)
combobox_1.set("Method")
combobox_1.configure(font=font_style)

#For the Graph
combobox_2 = customtkinter.CTkComboBox(frame, values=["For each year", "Whole period"])
combobox_2.pack(pady=5, padx=5)
combobox_2.set("Graph")
combobox_2.configure(font=font_style)

#Final FIND button
button = customtkinter.CTkButton(master = frame, text = "Find", command= retrieve_input)
button.pack(pady=12,padx=10)
button.configure(font=font_style)

root.mainloop()
 