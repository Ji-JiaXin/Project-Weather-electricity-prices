# User Interface

# pip install customtkinter
import customtkinter
import tkinter
import pandas as pd

import sys
# Add the folder path to the sys.path
sys.path.append("C:/Users/Sedláček/pr/Project-Weather-electricity-prices/Processing_and_graphs")
from Searching_first_diff import searching_difference

customtkinter.set_ctk_parent_class(tkinter.Tk)

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
final_data = pd.read_csv('C:/Users/Sedláček/pr/Project-Weather-electricity-prices/Processing_and_graphs/final_data.csv')
input_row = []

import pandas as pd  # Ensure pandas is imported at the top of your file

def retrieve_input():
    # Clear previous inputs to handle consecutive uses without restarting the app
    input_row.clear()

    # Collect input values from entry widgets and convert them to floats
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
        return  # Exits the function if conversion fails

    try:
        threshold = float(entry_var_threshold.get())
    except ValueError:
        print("Please enter a valid numeric value for the threshold.")
        return  # Exits the function if conversion fails

    # Call the function with the DataFrame
    similar_periods = searching_difference(input_temperatures, final_data, threshold)
    for index, period in enumerate(similar_periods):
            print(f"Similar period {index + 1}:\n", period, "\n")
    
    print('We have found', len(similar_periods), 'similar periods')
    # Your existing logic for handling the output from searching_difference follows...



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
optionmenu_1.set("Sources")

combobox_1 = customtkinter.CTkComboBox(frame, values=["Simple sq. diff", "Differenceated"])
combobox_1.pack(pady=10, padx=10)
combobox_1.set("Method")

button = customtkinter.CTkButton(master = frame, text = "Find", command= retrieve_input)
button.pack(pady=12,padx=10)

root.mainloop()
 