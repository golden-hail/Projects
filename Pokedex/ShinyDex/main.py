# This code is generated using PyUIbuilder: https://pyuibuilder.com

import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from pyuiWidgets.imageLabel import ImageLabel
from pyuiWidgets.listBox import ScrollableListbox

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

## Main menu set up
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

frame = tk.Frame(master=main)
frame.config(bg="#EDECEC")
frame.place(x=528, y=297, width=100, height=100)

style.configure("img_label.TLabel", background="#d62929", foreground="#000", anchor="center")
img_label = ImageLabel(master=main, image_path=os.path.join(BASE_DIR, "assets", "images", "bluebutton.png"), text="", compound=tk.TOP, mode="cover")
img_label.configure(anchor="center")
img_label.place(x=0, y=0, width=112, height=107)

style.configure("title.TLabel", background="#d62929", foreground="#ffffff", font=("Arial", 50, "bold"), anchor="center")
title = ttk.Label(master=main, text="Shiny Dex", style="title.TLabel")
title.configure(anchor="center")
title.place(x=231, y=0, width=371, height=100)

style.configure("entry_in_msg.TLabel", background="#566899", foreground="#ffffff", font=("Arial", 17, "bold"), anchor="center")
entry_in_msg = ttk.Label(master=main, text="Enter your shiny Pokemon data:", style="entry_in_msg.TLabel")
entry_in_msg.configure(anchor="center")
entry_in_msg.place(x=297, y=113, width=490, height=33)

## !Pokemon selection list
style.configure("pokemon.TLabel", background="#d62929", foreground="#e9dfdf", font=("Arial", 25), anchor="w")
pokemon = ttk.Label(master=main, text="Pokemon", style="pokemon.TLabel")
pokemon.configure(anchor="w")
pokemon.place(x=31, y=115, width=222, height=38)

## Choose from Pokemon List
list_box_items = ["a","b","c","d","e","f","g","h"]
list_box = ScrollableListbox(parent=main, scrollx=False, scrolly=True)

for i in list_box_items:
	list_box.insert(tk.END, i)

list_box.config(bg="#E4E2E2", fg="#000000", font=("Arial", 20))
list_box.place(x=33, y=156, width=227, height=302)

## Nickname
style.configure("nickname.TLabel", background="#d62929", foreground="#ffffff", font=("Arial", 15), anchor="w")
nickname = ttk.Label(master=main, text="Nickname", style="nickname.TLabel")
nickname.configure(anchor="w")
nickname.place(x=297, y=396, width=96, height=32)

## Capture date
style.configure("cap_date.TLabel", background="#d62929", foreground="#e9dfdf", font=("Arial", 15), anchor="w")
cap_date = ttk.Label(master=main, text="Date of Capture", style="cap_date.TLabel")
cap_date.configure(anchor="w")
cap_date.place(x=297, y=264, width=202, height=30)

style.configure("data_captured.TEntry", fieldbackground="#d9d4d4", foreground="#000", font=("Arial", 15))

data_captured = ttk.Entry(master=main, style="data_captured.TEntry")
data_captured.place(x=299, y=297, width=197, height=28)

## Location Caught
style.configure("location.TEntry", fieldbackground="#d9d4d4", foreground="#000", font=("Arial", 15))

location = ttk.Entry(master=main, style="location.TEntry")
location.place(x=297, y=363, width=200, height=28)

style.configure("location_in.TLabel", background="#d62929", foreground="#f7f1f1", font=("Arial", 15), anchor="w")
location_in = ttk.Label(master=main, text="Location", style="location_in.TLabel")
location_in.configure(anchor="w")
location_in.place(x=297, y=330, width=80, height=29)

style.configure("gender.TLabel", background="#d62929", foreground="#f5f1f1", font=("Arial", 15), anchor="w")
gender = ttk.Label(master=main, text="Gender", style="gender.TLabel")
gender.configure(anchor="w")
gender.place(x=528, y=264, width=79, height=32)



## Gender
radio_button_var = tk.IntVar()
style.configure("radio_button.TRadiobutton", background="#E4E2E2", foreground="#000", relief=tk.FLAT)
style.map("radio_button.TRadiobutton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

# unknown first? / as default
radio_button_0 = ttk.Radiobutton(master=frame, variable=radio_button_var, text="Male", value=0, style="radio_button.TRadiobutton")
radio_button_0.pack(side=tk.TOP, fill="both", expand=True, padx=0, pady=0)

radio_button_1 = ttk.Radiobutton(master=frame, variable=radio_button_var, text="Female", value=1, style="radio_button.TRadiobutton")
radio_button_1.pack(side=tk.TOP, fill="both", expand=True, padx=0, pady=0)

radio_button_2 = ttk.Radiobutton(master=frame, variable=radio_button_var, text="No Gender", value=2, style="radio_button.TRadiobutton")
radio_button_2.pack(side=tk.TOP, fill="both", expand=True, padx=0, pady=0)

radio_button_3 = ttk.Radiobutton(master=frame, variable=radio_button_var, text="Unknown", value=3, style="radio_button.TRadiobutton")
radio_button_3.pack(side=tk.TOP, fill="both", expand=True, padx=0, pady=0)

## Encounters
style.configure("encounters.TEntry", fieldbackground="#d9d4d4", foreground="#000", font=("", 15))

encounters = ttk.Entry(master=main, style="encounters.TEntry")
encounters.place(x=528, y=429, width=101, height=29)

style.configure("encount.TLabel", background="#d62929", foreground="#ffffff", font=("Arial", 15), anchor="center")
encount = ttk.Label(master=main, text="Encounters   ", style="encount.TLabel")
encount.configure(anchor="center")
encount.place(x=516, y=399, width=106, height=30)



## other nickname
style.configure("nickname.TEntry", fieldbackground="#d9d4d4", foreground="#000", font=("Arial", 15))

nickname = ttk.Entry(master=main, style="nickname.TEntry")
nickname.place(x=297, y=429, width=202, height=28)

## Variation
style.configure("variation.TCombobox", fieldbackground="#d9d4d4", foreground="#000", font=("Arial", 15, ))
variation_options = ["Alolan","Galarian","Hisuian","original"]
variation_var = tk.StringVar(value="Variation?")
variation = ttk.Combobox(main, textvariable=variation_var, values=variation_options, style="variation.TCombobox")
variation.place(x=297, y=231, width=195, height=31)

## Original Game
style.configure("original_game.TCombobox", fieldbackground="#d9d4d4", foreground="#000", font=("Arial", 15, ))
original_game_options = ['Yellow', 'Silver', 'Gold', 'Crystal', 'Ruby', 'Sapphire', 'Emerald', 
           'Fire Red', 'Leaf Green', 'Diamond', 'Pearl', 'Platinum', 'HeartGold', 'Soulsilver', 
           'Black', 'White', 'Black 2', 'White 2', 'X', 'Y', 'Alpha Sapphire', 'Omega Ruby',
           'Pokemon Go', 'Sun', 'Moon', 'Ultra Sun', 'Ultra Moon', "Let's Go Eevee", "Let's Go Pikachu", 
           'Sword', 'Shield', 'Shining Pearl', 'Legends of Arceus', 'Scarlet', 'Voilet', 'Legends ZA']
original_game_var = tk.StringVar(value="Game Found In")
original_game = ttk.Combobox(main, textvariable=original_game_var, values=original_game_options, style="original_game.TCombobox")
original_game.place(x=297, y=165, width=193, height=34)

## Nature
style.configure("nature_menu.TCombobox", fieldbackground="#d9d4d4", foreground="#000", font=("Arial", 15, ))
nature_options = ['Relaxed', 'Adamant', 'Naive', 'Hardy', 'Impish', 'Rash', 'Lonely',
       'Jolly', 'Quirky', 'Lax', 'Careful', 'Modest', 'Brave',
       'Sassy', 'Hasty', 'Bashful', 'Quiet', 'Mild', 'Naughty', 'Docile',
       'Bold', 'Gentle', 'Serious', 'Calm', 'Timid', '-'] 
nature_options.sort()
nature_var = tk.StringVar(value="Nature")
nature_menu = ttk.Combobox(main, textvariable=nature_var, values=nature_options, style="nature_menu.TCombobox")
nature_menu.place(x=528, y=231, width=125, height=33)

## Ball
style.configure("ball.TCombobox", fieldbackground="#d9d4d4", foreground="#000", font=("Arial", 15, ))
ball_options = ["Poke Ball", "Great Ball", "Ultra Ball", "Master Ball", 
                "Safari Ball", "Sport Ball", "Premier Ball", "Cherish Ball",
                "Park Ball", "Beast Ball", "Origin Ball", "Net Ball", "Dive Ball",
                "Nest Ball", "Repeat Ball", "Timer Ball", "Luxury Ball", "Heal Ball",
                "Quick Ball", "Dusk Ball", "Dream Ball", "Fast Ball", "Heavy Ball",
                "Level Ball", "Love Ball", "Moon Ball", "Lure Ball", "Feather Ball",
                "Wing Ball", "Jet Ball", "Heavy Ball", "Leaden Ball", "Gigaton Ball"]
ball_options.sort()
ball_var = tk.StringVar(value="Ball")
ball = ttk.Combobox(main, textvariable=ball_var, values=ball_options, style="ball.TCombobox")
ball.place(x=693, y=231, width=95, height=36)

# Shiny Hunting Method
style.configure("hunt_method.TCombobox", fieldbackground="#d9d4d4", foreground="#000", font=("Arial", 15, ))
hunt_method_options = ["option 1"]
hunt_method_var = tk.StringVar(value="Hunting Method")
hunt_method = ttk.Combobox(main, textvariable=hunt_method_var, values=hunt_method_options, style="hunt_method.TCombobox")
hunt_method.place(x=528, y=165, width=258, height=31)

## Description
style.configure("notes.TLabel", background="#d62929", foreground="#e9dfdf", font=("Arial", 18), anchor="sw")
notes = ttk.Label(master=main, text="Notes on Capture", style="notes.TLabel")
notes.configure(anchor="sw")
notes.place(x=33, y=462, width=220, height=37)

description = tk.Text(master=main)
description.config(bg="#d9d4d4", fg="#000", font=("Arial", 16))
description.place(x=33, y=495, width=759, height=106)

## Submit entry buttton (pipe function)
style.configure("button.TButton", background="#566899", foreground="#f6f9fc", font=("Arial", 20, "bold"))
style.map("button.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button = ttk.Button(master=main, text="Submit", style="button.TButton")
button.place(x=660, y=293, width=130, height=167)

main.mainloop()