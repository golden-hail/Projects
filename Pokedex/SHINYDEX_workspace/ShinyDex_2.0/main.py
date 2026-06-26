# This code is generated using PyUIbuilder: https://pyuibuilder.com

import os
import tkinter as tk
from tkinter import ttk
# from PIL import Image, ImageTk
from pyuiWidgets.imageLabel import ImageLabel
from pyuiWidgets.listBox import ScrollableListbox
import pandas as pd

nat_dex = pd.read_excel('Shiny_Dex_og.xlsx', sheet_name = 'pokedex')
goog_dex = pd.read_excel('Shiny_Dex_og.xlsx', sheet_name = 'googdex')

def add_2_shiny_db():
    # Auto calculate entry No to database
    # import dex to add new entry
    dex_raw = pd.read_excel('Shiny_Dex.xlsx', sheet_name = 'shiny_dex')
    # drop bad columns
    cols_2_drop = dex_raw.filter(regex=r'Unnamed:').columns
    dex_raw = dex_raw.drop(columns=cols_2_drop)
    # get next entry number
    entry = dex_raw['entryNo'].max() + 1 
    
    # get selected Pokemon
    selected_indices = mon_listbox.curselection() # Do i have an error for thisif they don't pick any mon??
    # check if the user has selected a mon
    if selected_indices:
        # get the first index from the tuple
        index = selected_indices[0] 
        mon = mon_listbox.get(index) 
        # find the NdexNo based on the name of the mon
        # NdexNo where nat_dex["Pokemon"] == mon
        mon_deets = nat_dex.loc[nat_dex["Pokemon"] == mon]
        no = mon_deets.iloc[0]['NdexNo'] 
    else:
        mon = 'Fake Mon'
        no = 0 
    breakpoint()
    # get index of where "Hisuian" is a part of the entry
    # Check that variation of mon exists
    variat = variat_menu.get()
    # if variat == 'Hisuian':
    #     hisui = nat_dex[nat_dex['Pokemon'].str.contains('Hisuian')]
    #     hisui.[hisui['Pokemon']].str.contains(mon)
    #     if mon in hisui:
            
    # elif variat == "Alolan":
    #     alolan = nat_dex[nat_dex['Pokemon'].str.contains('Alolan')]
    # elif variat == "Galarian":
    #     galarian = nat_dex[nat_dex['Pokemon'].str.contains('Galarian')]
    # else:
    #     pass
    # on spreadsheet, change each "Region" column to the actual region the vairaiants are from
            
    # for i in nat_dex["Pokemon"]
    # if variat:
        # check nat_dex to see if valid variat nat_dex["Pokemon"] exists
    # gender = gender_in.get()
    gender = 'female'
    og_game = og_game_entry.get()
    loca = loc_entry.get()
    date_cap = [] #! def check_date_cap:
    # method = hunt_entry.get() 
    method = ""
    nickname = ni_name_entry.get()
    nature = natr_menu.get()
    ball = ball_menu.get()
    encounts = encount_entry.get()
    descript =  description.get("1.0", "end-1c")
    
    # Input Trainer Name to Sign in
    trainer = "Fake-o Joe"
    form = ""
    
    # add the entry to the Shiny Dex database 
    dex_raw.loc[len(dex_raw)] = [entry, no, mon, variat, form, gender, 
                                 og_game, loca, date_cap, method, nickname, 
                                 nature, ball, encounts, descript, trainer]
    #! save output to new excel
    # Export to xlsx
    dex_raw.to_excel('Shiny_Dex.xlsx', sheet_name = "shiny_dex", index = False)

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

frame = tk.Frame(master=main)
frame.config(bg="#EDECEC")
frame.place(x=528, y=297, width=100, height=100)

description = tk.Text(master=main)
description.config(bg="#d9d4d4", fg="#000", font=("Arial", 16))
description.place(x=33, y=495, width=759, height=106)

## Select Pokemon
style.configure("mon_lab.TLabel", background="#d62929", foreground="#e9dfdf", font=("Arial", 30), anchor="w")
mon_lab = ttk.Label(master=main, text="Pokemon", style="mon_lab.TLabel")
mon_lab.configure(anchor="w")
mon_lab.place(x=31, y=112, width=229, height=43)

## Choose from Pokemon List
mon_list = nat_dex["Pokemon"]
mon_listbox = ScrollableListbox(parent=main, scrollx=False, scrolly=True, exportselection=False)

for i in mon_list:
	mon_listbox.insert(tk.END, i)

mon_listbox.config(bg="#E4E2E2", fg="#000000", font=("Arial", 15))
mon_listbox.place(x=33, y=161, width=228, height=297)

## Date Entry
style.configure("date_lab.TLabel", background="#d62929", foreground="#e9dfdf", font=("Arial", 15), anchor="w")
date_lab = ttk.Label(master=main, text="Date of Capture", style="date_lab.TLabel")
date_lab.configure(anchor="w")
date_lab.place(x=297, y=264, width=202, height=30)

style.configure("date_entry.TEntry", fieldbackground="#d9d4d4", foreground="#000", font=("Arial", 15))

date_entry = ttk.Entry(master=main, style="date_entry.TEntry")
date_entry.place(x=299, y=297, width=197, height=28)

## Location Entry
style.configure("loc_entry.TEntry", fieldbackground="#d9d4d4", foreground="#000", font=("Arial", 15))

loc_entry = ttk.Entry(master=main, style="loc_entry.TEntry")
loc_entry.place(x=297, y=363, width=200, height=28)

style.configure("loc_lab.TLabel", background="#d62929", foreground="#f7f1f1", font=("Arial", 15), anchor="w")
loc_lab = ttk.Label(master=main, text="Location", style="loc_lab.TLabel")
loc_lab.configure(anchor="w")
loc_lab.place(x=297, y=330, width=80, height=29)

## Gender Selection
style.configure("gender_lab.TLabel", background="#d62929", foreground="#f5f1f1", font=("Arial", 15), anchor="w")
gender_lab = ttk.Label(master=main, text="Gender", style="gender_lab.TLabel")
gender_lab.configure(anchor="w")
gender_lab.place(x=528, y=264, width=79, height=32)

gender_sel_var = tk.IntVar()
style.configure("gender_sel.TRadiobutton", background="#E4E2E2", foreground="#000", relief=tk.FLAT)
style.map("gender_sel.TRadiobutton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

gender_sel_0 = ttk.Radiobutton(master=frame, variable=gender_sel_var, text="Male", value=0, style="gender_sel.TRadiobutton")
gender_sel_0.pack(side=tk.TOP, fill="both", expand=True, padx=0, pady=0)

gender_sel_1 = ttk.Radiobutton(master=frame, variable=gender_sel_var, text="Female", value=1, style="gender_sel.TRadiobutton")
gender_sel_1.pack(side=tk.TOP, fill="both", expand=True, padx=0, pady=0)

gender_sel_2 = ttk.Radiobutton(master=frame, variable=gender_sel_var, text="No Gender", value=2, style="gender_sel.TRadiobutton")
gender_sel_2.pack(side=tk.TOP, fill="both", expand=True, padx=0, pady=0)

gender_sel_3 = ttk.Radiobutton(master=frame, variable=gender_sel_var, text="Unknown", value=3, style="gender_sel.TRadiobutton")
gender_sel_3.pack(side=tk.TOP, fill="both", expand=True, padx=0, pady=0)

## Encounters Entry
style.configure("enc_lab.TLabel", background="#d62929", foreground="#ffffff", font=("Arial", 15), anchor="center")
enc_lab = ttk.Label(master=main, text="Encounters   ", style="enc_lab.TLabel")
enc_lab.configure(anchor="center")
enc_lab.place(x=527, y=399, width=106, height=30)

style.configure("encount_entry.TEntry", fieldbackground="#d9d4d4", foreground="#000", font=("", 15))

encount_entry = ttk.Entry(master=main, style="encount_entry.TEntry")
encount_entry.place(x=528, y=429, width=101, height=29)

## Nickname Entry
style.configure("niname_lab.TLabel", background="#d62929", foreground="#ffffff", font=("Arial", 15), anchor="w")
niname_lab = ttk.Label(master=main, text="Nickname", style="niname_lab.TLabel")
niname_lab.configure(anchor="w")
niname_lab.place(x=297, y=396, width=96, height=32)

style.configure("ni_name_entry.TEntry", fieldbackground="#d9d4d4", foreground="#000", font=("Arial", 15))

ni_name_entry = ttk.Entry(master=main, style="ni_name_entry.TEntry")
ni_name_entry.place(x=297, y=429, width=202, height=28)

## Variation Selection 
style.configure("variation_lab.TLabel", background="#d62929", foreground="#e9dfdf", font=("Arial", 15), anchor="w")
variation_lab = ttk.Label(master=main, text="Variation?", style="variation_lab.TLabel")
variation_lab.configure(anchor="w")
variation_lab.place(x=295, y=202, width=202, height=30)

style.configure("variat_menu.TCombobox", fieldbackground="#d9d4d4", foreground="#000", font=("Arial", 15, ))
variat_menu_options = ["Alolan","Galarian","Hisuian","N/A"]
variat_menu_var = tk.StringVar(value="")
variat_menu = ttk.Combobox(main, textvariable=variat_menu_var, values=variat_menu_options, style="variat_menu.TCombobox")
variat_menu.place(x=297, y=231, width=195, height=31)

## Game Selection
style.configure("og_game_lab.TLabel", background="#d62929", foreground="#e9dfdf", font=("Arial", 15), anchor="w")
og_game_lab = ttk.Label(master=main, text="Game Found In", style="og_game_lab.TLabel")
og_game_lab.configure(anchor="w")
og_game_lab.place(x=295, y=136, width=202, height=30)

style.configure("og_game_entry.TCombobox", fieldbackground="#d9d4d4", foreground="#000", font=("Arial", 15, ))
og_game_entry_options = ['Yellow', 'Silver', 'Gold', 'Crystal', 'Ruby', 'Sapphire', 'Emerald', 
           'Fire Red', 'Leaf Green', 'Diamond', 'Pearl', 'Platinum', 'HeartGold', 'Soulsilver', 
           'Black', 'White', 'Black 2', 'White 2', 'X', 'Y', 'Alpha Sapphire', 'Omega Ruby',
           'Pokemon Go', 'Sun', 'Moon', 'Ultra Sun', 'Ultra Moon', "Let's Go Eevee", "Let's Go Pikachu", 
           'Sword', 'Shield', 'Shining Pearl', 'Legends of Arceus', 'Scarlet', 'Voilet', 'Legends ZA']
og_game_entry_var = tk.StringVar(value="")
og_game_entry = ttk.Combobox(main, textvariable=og_game_entry_var, values=og_game_entry_options, style="og_game_entry.TCombobox")
og_game_entry.place(x=297, y=165, width=193, height=34)

## Nature Selection 
style.configure("natr_lab.TLabel", background="#d62929", foreground="#e9dfdf", font=("Arial", 15), anchor="w")
natr_lab = ttk.Label(master=main, text="Nature", style="natr_lab.TLabel")
natr_lab.configure(anchor="w")
natr_lab.place(x=527, y=203, width=129, height=29)

style.configure("natr_menu.TCombobox", fieldbackground="#d9d4d4", foreground="#000", font=("Arial", 15, ))
natr_menu_ops = ['Relaxed', 'Adamant', 'Naive', 'Hardy', 'Impish', 'Rash', 'Lonely',
       'Jolly', 'Quirky', 'Lax', 'Careful', 'Modest', 'Brave',
       'Sassy', 'Hasty', 'Bashful', 'Quiet', 'Mild', 'Naughty', 'Docile',
       'Bold', 'Gentle', 'Serious', 'Calm', 'Timid', '-'] 
natr_menu_ops.sort()
natr_menu_var = tk.StringVar(value="")
natr_menu = ttk.Combobox(main, textvariable=natr_menu_var, values=natr_menu_ops, style="natr_menu.TCombobox")
natr_menu.place(x=528, y=231, width=125, height=33)

## Ball Selection
style.configure("ball_lab.TLabel", background="#d62929", foreground="#e9dfdf", font=("Arial", 15), anchor="w")
ball_lab = ttk.Label(master=main, text="Ball", style="ball_lab.TLabel")
ball_lab.configure(anchor="w")
ball_lab.place(x=689, y=203, width=109, height=29)

style.configure("ball_menu.TCombobox", fieldbackground="#d9d4d4", foreground="#000", font=("Arial", 15, ))
ball_ops = ["Poke Ball", "Great Ball", "Ultra Ball", "Master Ball", 
                "Safari Ball", "Sport Ball", "Premier Ball", "Cherish Ball",
                "Park Ball", "Beast Ball", "Origin Ball", "Net Ball", "Dive Ball",
                "Nest Ball", "Repeat Ball", "Timer Ball", "Luxury Ball", "Heal Ball",
                "Quick Ball", "Dusk Ball", "Dream Ball", "Fast Ball", "Heavy Ball",
                "Level Ball", "Love Ball", "Moon Ball", "Lure Ball", "Feather Ball",
                "Wing Ball", "Jet Ball", "Heavy Ball", "Leaden Ball", "Gigaton Ball"]
ball_ops.sort()
ball_menu_var = tk.StringVar(value="")
ball_menu = ttk.Combobox(main, textvariable=ball_menu_var, values=ball_ops, style="ball_menu.TCombobox")
ball_menu.place(x=693, y=231, width=95, height=36)

## Hunt Selection
style.configure("hunt_lab.TLabel", background="#d62929", foreground="#e9dfdf", font=("Arial", 15), anchor="w")
hunt_lab = ttk.Label(master=main, text="Shiny Hunting Method", style="hunt_lab.TLabel")
hunt_lab.configure(anchor="w")
hunt_lab.place(x=526, y=134, width=202, height=30)

style.configure("hunt_entry.TCombobox", fieldbackground="#d9d4d4", foreground="#000", font=("Arial", 15, ))
hunt_entry_options = ['Event', 'Chain Fishing', 'Horde Encounters', 'Random Encounters',
       'Catch Combo', 'Spotlight Hour', 'Community Day', 'Battle Method',
       'Raid Den Event', 'Soft Resets', 'Raid Battle', 'Masuda Method',
       'Dynamax Adventures', 'Radar Method', 'Friend Safari',
       'Hoard Encounters', 'Gift', 'Ultra Space Wilds', 'SOS Chaining',
       'Community day', 'Mass Outbreaks', 'Random Encounter', 'DV Method']
hunt_entry_var = tk.StringVar(value="")
hunt_entry = ttk.Combobox(main, textvariable=hunt_entry_var, values=hunt_entry_options, style="hunt_entry.TCombobox")
hunt_entry.place(x=528, y=165, width=258, height=31)

## Description Entry
style.configure("descr_lab.TLabel", background="#d62929", foreground="#e9dfdf", font=("Arial", 16), anchor="sw")
descr_lab = ttk.Label(master=main, text="Notes on Capture", style="descr_lab.TLabel")
descr_lab.configure(anchor="sw")
descr_lab.place(x=33, y=455, width=220, height=36)

# Aesthetics 
style.configure("label.TLabel", background="#d62929", foreground="#ffffff", font=("Arial", 50, "bold"), anchor="center")
label = ttk.Label(master=main, text="Shiny Dex", style="label.TLabel")
label.configure(anchor="center")
label.place(x=231, y=0, width=371, height=100)

style.configure("menu_msg.TLabel", background="#566899", foreground="#ffffff", font=("Arial", 17, "bold"), anchor="center")
menu_msg = ttk.Label(master=main, text="Enter your shiny Pokemon data:", style="menu_msg.TLabel")
menu_msg.configure(anchor="center")
menu_msg.place(x=293, y=102, width=490, height=33)

style.configure("dex_button.TLabel", background="#d62929", foreground="#000", anchor="center")
dex_button = ImageLabel(master=main, image_path=os.path.join(BASE_DIR, "assets", "images", "bluebutton.png"), text="", compound=tk.TOP, mode="cover")
dex_button.configure(anchor="center")
dex_button.place(x=9, y=10, width=116, height=85)

# Submit Entry
style.configure("submit_2_db.TButton", background="#566899", foreground="#f6f9fc", font=("Arial", 20, "bold"))
style.map("submit_2_db.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

submit_2_db = ttk.Button(master=main, text="Submit", style="submit_2_db.TButton", command=add_2_shiny_db)
submit_2_db.place(x=660, y=293, width=130, height=167)

main.mainloop()