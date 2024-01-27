# User Interface

# pip install customtkinter
import customtkinter
import tkinter

customtkinter.set_ctk_parent_class(tkinter.Tk)

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

def retrieve_input():
    input_value = entry_var.get()
    print("The entered value is:", input_value)

root = customtkinter.CTk()
root.geometry("400x680")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text = "Input Values")
label.pack(pady=10, padx=10)

entry_var = tkinter.StringVar()

entry_3 = customtkinter.CTkEntry(master=frame, placeholder_text="1st temperature",textvariable=entry_var)
entry_3.pack(pady=10, padx=10)

entry_4 = customtkinter.CTkEntry(master=frame, placeholder_text="2st temperature")
entry_4.pack(pady=10, padx=10)

entry_5 = customtkinter.CTkEntry(master=frame, placeholder_text="3st temperature")
entry_5.pack(pady=10, padx=10)

entry_6 = customtkinter.CTkEntry(master=frame, placeholder_text="4st temperature")
entry_6.pack(pady=10, padx=10)

entry_7 = customtkinter.CTkEntry(master=frame, placeholder_text="5st temperature")
entry_7.pack(pady=10, padx=10)

entry_8 = customtkinter.CTkEntry(master=frame, placeholder_text="6st temperature")
entry_8.pack(pady=10, padx=10)

entry_9 = customtkinter.CTkEntry(master=frame, placeholder_text="7st temperature")
entry_9.pack(pady=10, padx=10)

entry_10 = customtkinter.CTkEntry(master=frame, placeholder_text="Threshold")
entry_10.pack(pady=10, padx=10)


optionmenu_1 = customtkinter.CTkOptionMenu(frame, values=["Gen wind offshore", 
            "Gen other conven.", "Gen other renew.", "Gen wind onshore", "Gen photovolt",
            "Gen pumped storage", "Total consum.", "Consum. pumped storg."])
optionmenu_1.pack(pady=10, padx=10)
optionmenu_1.set("Sources")

combobox_1 = customtkinter.CTkComboBox(frame, values=["Simple sq. diff", "Differenceated"])
combobox_1.pack(pady=10, padx=10)
combobox_1.set("Method")

button = customtkinter.CTkButton(master = frame, text = "Find", command= retrieve_input)
button.pack(pady=12,padx=10)

root.mainloop()





import customtkinter as ctk

root = ctk.CTk()
frame = ctk.CTkFrame(root)
frame.pack(padx=10, pady=10)

entry_3 = ctk.CTkEntry(master=frame, placeholder_text="1st temperature")
entry_3.pack(pady=10, padx=10)

root.mainloop()
