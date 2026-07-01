import pandas as pd

dex_raw = pd.read_excel('Shiny_Dex.xlsx', sheet_name = 'shiny_dex')
nat_dex = pd.read_excel('Shiny_Dex.xlsx', sheet_name = 'pokedex')
dex_raw = dex_raw.drop(["Unnamed: 16"], axis = 1)

import tkinter as tk
from tkinter import ttk

def add_2_shiny_db():
    # Use .get() to retrieve the currently selected text in each input
    
    # Auto calculate entry No to database
    entry = dex_raw['entryNo'].max() + 1 
    #! Need to autolook this up based on Pokemon Name in future
    no = 0
    mon = combo_mon.get()
    variat = []
    form = []
    gender = []
    og_game = combo_game.get()
    loca = []
    date_cap = []
    meth = []
    nickname = niname.get()
    nature = combo_natr.get()
    ball = combo_ball.get()
    encounts = [0]
    description = ''
    
    # Input Trainer Name to Sign in
    user = "Fake-o Joe"
    
    # display inputs
    label.config(text=f"Selected: {entry}, {no}, {mon}, {variat}, {form}, {gender}, {og_game}, {loca}, {date_cap}, {meth}, {nature}, {ball}, {nickname}, {encounts}, {description}, {user}")
    
    # add the entry to the Shiny Dex database 
    dex_raw.loc[len(dex_raw)] = [entry, no, mon, variat, form, gender, 
                                 og_game, loca, date_cap, meth, nickname, 
                                 nature, ball, encounts, description, user]
    
    #! save output to new excel
    # Export to xlsx
    dex_raw.to_excel('dexport.xlsx', sheet_name = "Sheet_12345")

# Initialize main window
root = tk.Tk()
root.title("Shiny Catch Details")
root.geometry("1000x1000")

# Create combobox for selecting the mon
mon_options = list(nat_dex['Pokemon'])
combo_mon = ttk.Combobox(root, values=mon_options, state="readonly")
combo_mon.set("Select a Pokemon") 
combo_mon.pack(pady=10)

# variat = []
# form = []

# Combo box for game of origin
game_options = ['Yellow', 'Silver', 'Gold', 'Crystal', 'Ruby', 'Sapphire', 'Emerald', 
           'Fire Red', 'Leaf Green', 'Diamond', 'Pearl', 'Platinum', 'HeartGold', 'Soulsilver', 
           'Black', 'White', 'Black 2', 'White 2', 'X', 'Y', 'Alpha Sapphire', 'Omega Ruby',
           'Pokemon Go', 'Sun', 'Moon', 'Ultra Sun', 'Ultra Moon', "Let's Go Eevee", "Let's Go Pikachu", 
           'Sword', 'Shield', 'Shining Pearl', 'Legends of Arceus', 'Scarlet', 'Voilet', 'Legends ZA']

combo_game = ttk.Combobox(root, values=game_options, state="readonly")
combo_game.set("Select the Game of Origin") 
combo_game.pack(pady=8)

# loca = []
# date_cap = [] # need to figure out date-time
# meth = []

# Combo box for Nature
natr_options = ['Relaxed', 'Adamant', 'Naive', 'Hardy', 'Impish', 'Rash', 'Lonely',
       'Jolly', 'Quirky', 'Lax', 'Careful', 'Modest', 'Brave',
       'Sassy', 'Hasty', 'Bashful', 'Quiet', 'Mild', 'Naughty', 'Docile',
       'Bold', 'Gentle', 'Serious', 'Calm', 'Timid', '-'] # replace nans with unknown in dataset later (show code that does this in portfolio??)

natr_options.sort()

combo_natr = ttk.Combobox(root, values=natr_options, state="readonly")
combo_natr.set("Select a Nature") # make default entry '-'
combo_natr.pack(pady=10)

# Define the choices of Pokeball
ball_options = ["Poke Ball", "Great Ball", "Ultra Ball", "Master Ball", 
                "Safari Ball", "Sport Ball", "Premier Ball", "Cherish Ball",
                "Park Ball", "Beast Ball", "Origin Ball", "Net Ball", "Dive Ball",
                "Nest Ball", "Repeat Ball", "Timer Ball", "Luxury Ball", "Heal Ball",
                "Quick Ball", "Dusk Ball", "Dream Ball", "Fast Ball", "Heavy Ball",
                "Level Ball", "Love Ball", "Moon Ball", "Lure Ball", "Feather Ball",
                "Wing Ball", "Jet Ball", "Heavy Ball", "Leaden Ball", "Gigaton Ball"]

ball_options.sort()

# Create the Combobox for selecting the Pokeball
combo_ball = ttk.Combobox(root, values=ball_options, state="readonly")
combo_ball.set("Select a Pokeball") 
combo_ball.pack(pady=10)

# Textbox for Nickname
    # 1. Create and pack the title label
title_niname = tk.Label(root, text="Nickname:")
title_niname.pack(pady=(5, 0)) # Adds spacing above the label

niname = tk.Entry(root, width=25)
niname.pack(pady=0)

# Create a button to trigger action
button = tk.Button(root, text="Submit", command=add_2_shiny_db) # this command will be the link to a function I write where I take in for the Add New Pokemon function
button.pack(pady=10)

# Create a label to display output
label = tk.Label(root, text="")
label.pack(pady=20)

root.mainloop()



