# This code is generated using PyUIbuilder: https://pyuibuilder.com

import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from pyuiWidgets.imageLabel import ImageLabel
from pyuiWidgets.listBox import ScrollableListbox

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


main = tk.Tk()
main.title("Create New Shiny Entry")
main.config(bg="#d62929")
main.geometry("829x639")
main.update_idletasks()

geometryX = 0
geometryY = 0

main.geometry("+%d+%d"%(geometryX, geometryY))
main.resizable(False, False)



style = ttk.Style(main)
style.theme_use("clam")


style.configure("label.TLabel", background="#d62929", foreground="#000", anchor="center")
label = ImageLabel(master=main, image_path=os.path.join(BASE_DIR, "assets", "images", "bluebutton.png"), text="", compound=tk.TOP, mode="cover")
label.configure(anchor="center")
label.place(x=0, y=0, width=112, height=107)

list_box_items = ["a","b","c","d","e","f","g","h"]
list_box = ScrollableListbox(parent=main, scrollx=False, scrolly=True)

for i in list_box_items:
	list_box.insert(tk.END, i)

list_box.config(bg="#E4E2E2", fg="#000000", font=("Arial", 20))
list_box.place(x=33, y=156, width=227, height=302)

style.configure("label1.TLabel", background="#d62929", foreground="#ffffff", font=("Arial", 15), anchor="w")
label1 = ttk.Label(master=main, text="Nickname", style="label1.TLabel")
label1.configure(anchor="w")
label1.place(x=297, y=396, width=96, height=32)

style.configure("location.TEntry", fieldbackground="#d9d4d4", foreground="#000", font=("Arial", 15))

location = ttk.Entry(master=main, style="location.TEntry")
location.place(x=297, y=363, width=200, height=28)

style.configure("label2.TLabel", background="#d62929", foreground="#f7f1f1", font=("Arial", 15), anchor="w")
label2 = ttk.Label(master=main, text="Location", style="label2.TLabel")
label2.configure(anchor="w")
label2.place(x=297, y=330, width=80, height=29)

style.configure("label3.TLabel", background="#d62929", foreground="#e9dfdf", font=("Arial", 15), anchor="w")
label3 = ttk.Label(master=main, text="Date of Capture", style="label3.TLabel")
label3.configure(anchor="w")
label3.place(x=297, y=264, width=202, height=30)

style.configure("data_captured.TEntry", fieldbackground="#d9d4d4", foreground="#000", font=("Arial", 15))

data_captured = ttk.Entry(master=main, style="data_captured.TEntry")
data_captured.place(x=299, y=297, width=197, height=28)

style.configure("label4.TLabel", background="#d62929", foreground="#f5f1f1", font=("Arial", 15), anchor="w")
label4 = ttk.Label(master=main, text="Gender", style="label4.TLabel")
label4.configure(anchor="w")
label4.place(x=528, y=264, width=79, height=32)

frame = tk.Frame(master=main)
frame.config(bg="#EDECEC")
frame.place(x=528, y=297, width=100, height=100)

radio_button_var = tk.IntVar()
style.configure("radio_button.TRadiobutton", background="#E4E2E2", foreground="#000", relief=tk.FLAT)
style.map("radio_button.TRadiobutton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])


radio_button_0 = ttk.Radiobutton(master=frame, variable=radio_button_var, text="Male", value=0, style="radio_button.TRadiobutton")
radio_button_0.pack(side=tk.TOP, fill="both", expand=True, padx=0, pady=0)


radio_button_1 = ttk.Radiobutton(master=frame, variable=radio_button_var, text="Female", value=1, style="radio_button.TRadiobutton")
radio_button_1.pack(side=tk.TOP, fill="both", expand=True, padx=0, pady=0)


radio_button_2 = ttk.Radiobutton(master=frame, variable=radio_button_var, text="No Gender", value=2, style="radio_button.TRadiobutton")
radio_button_2.pack(side=tk.TOP, fill="both", expand=True, padx=0, pady=0)


radio_button_3 = ttk.Radiobutton(master=frame, variable=radio_button_var, text="Unknown", value=3, style="radio_button.TRadiobutton")
radio_button_3.pack(side=tk.TOP, fill="both", expand=True, padx=0, pady=0)

style.configure("encounters.TEntry", fieldbackground="#d9d4d4", foreground="#000", font=("", 15))

encounters = ttk.Entry(master=main, style="encounters.TEntry")
encounters.place(x=528, y=429, width=101, height=29)

style.configure("label5.TLabel", background="#d62929", foreground="#ffffff", font=("Arial", 15), anchor="center")
label5 = ttk.Label(master=main, text="Encounters   ", style="label5.TLabel")
label5.configure(anchor="center")
label5.place(x=516, y=399, width=106, height=30)

style.configure("button.TButton", background="#566899", foreground="#f6f9fc", font=("Arial", 20, "bold"))
style.map("button.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button = ttk.Button(master=main, text="Submit", style="button.TButton")
button.place(x=660, y=293, width=130, height=167)

style.configure("nickname.TEntry", fieldbackground="#d9d4d4", foreground="#000", font=("Arial", 15))

nickname = ttk.Entry(master=main, style="nickname.TEntry")
nickname.place(x=297, y=429, width=202, height=28)

style.configure("variation.TCombobox", fieldbackground="#d9d4d4", foreground="#000", font=("Arial", 15, ))
variation_options = ["Alolan","Galarian","Hisuian","original"]
variation_var = tk.StringVar(value="Variation?")
variation = ttk.Combobox(main, textvariable=variation_var, values=variation_options, style="variation.TCombobox")
variation.place(x=297, y=231, width=195, height=31)

style.configure("original_game.TCombobox", fieldbackground="#d9d4d4", foreground="#000", font=("Arial", 15, ))
original_game_options = ["option 1"]
original_game_var = tk.StringVar(value="Game Found In")
original_game = ttk.Combobox(main, textvariable=original_game_var, values=original_game_options, style="original_game.TCombobox")
original_game.place(x=297, y=165, width=193, height=34)

style.configure("option_menu.TCombobox", fieldbackground="#d9d4d4", foreground="#000", font=("Arial", 15, ))
option_menu_options = ["option 1"]
option_menu_var = tk.StringVar(value="Nature")
option_menu = ttk.Combobox(main, textvariable=option_menu_var, values=option_menu_options, style="option_menu.TCombobox")
option_menu.place(x=528, y=231, width=125, height=33)

style.configure("option_menu1.TCombobox", fieldbackground="#d9d4d4", foreground="#000", font=("Arial", 15, ))
option_menu1_options = ["option 1"]
option_menu1_var = tk.StringVar(value="Ball")
option_menu1 = ttk.Combobox(main, textvariable=option_menu1_var, values=option_menu1_options, style="option_menu1.TCombobox")
option_menu1.place(x=693, y=231, width=95, height=36)

style.configure("option_menu2.TCombobox", fieldbackground="#d9d4d4", foreground="#000", font=("Arial", 15, ))
option_menu2_options = ["option 1"]
option_menu2_var = tk.StringVar(value="Hunting Method")
option_menu2 = ttk.Combobox(main, textvariable=option_menu2_var, values=option_menu2_options, style="option_menu2.TCombobox")
option_menu2.place(x=528, y=165, width=258, height=31)

style.configure("label6.TLabel", background="#566899", foreground="#ffffff", font=("Arial", 17, "bold"), anchor="center")
label6 = ttk.Label(master=main, text="Enter your shiny Pokemon data:", style="label6.TLabel")
label6.configure(anchor="center")
label6.place(x=297, y=113, width=490, height=33)

style.configure("label7.TLabel", background="#d62929", foreground="#e9dfdf", font=("Arial", 18), anchor="sw")
label7 = ttk.Label(master=main, text="Notes on Capture", style="label7.TLabel")
label7.configure(anchor="sw")
label7.place(x=33, y=462, width=220, height=37)

description = tk.Text(master=main)
description.config(bg="#d9d4d4", fg="#000", font=("Arial", 16))
description.place(x=33, y=495, width=759, height=106)

style.configure("label8.TLabel", background="#d62929", foreground="#ffffff", font=("Arial", 50, "bold"), anchor="center")
label8 = ttk.Label(master=main, text="Shiny Dex", style="label8.TLabel")
label8.configure(anchor="center")
label8.place(x=231, y=0, width=371, height=100)

style.configure("label9.TLabel", background="#d62929", foreground="#e9dfdf", font=("Arial", 32), anchor="w")
label9 = ttk.Label(master=main, text="Pokemon", style="label9.TLabel")
label9.configure(anchor="w")
label9.place(x=31, y=112, width=222, height=38)


main.mainloop()