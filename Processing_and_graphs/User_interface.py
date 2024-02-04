# User Interface

# pip install customtkinter
import customtkinter
import tkinter

customtkinter.set_ctk_parent_class(tkinter.Tk)

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

input_row = []

def retrieve_input():
    input_value_1 = entry_var_1.get()
    input_row.append(input_value_1)

    input_value_2 = entry_var_2.get()
    input_row.append(input_value_2)

    input_value_3 = entry_var_3.get()
    input_row.append(input_value_3)

    input_value_4 = entry_var_4.get()
    input_row.append(input_value_4)

    input_value_5 = entry_var_5.get()
    input_row.append(input_value_5)

    input_value_6 = entry_var_6.get()
    input_row.append(input_value_6)

    input_value_7 = entry_var_7.get()
    input_row.append(input_value_7)

    input_value_threshold = entry_var_threshold.get()
    input_row.append(input_value_threshold)
    

    source_energy = optionmenu_1.get()
    method_selected = combobox_1.get()

    print("Selected option from OptionMenu:", source_energy)
    print("Selected option from ComboBox:", method_selected)

    Teperature_input = ', '.join(input_row)
    print("The entered value is:", Teperature_input)






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
 