# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 16:25:43 2026

@author: aiaqu
"""

import pandas as pd

dex_raw = pd.read_excel('Shiny_Dex.xlsx', sheet_name = 'shiny_dex')
nat_dex = pd.read_excel('Shiny_Dex.xlsx', sheet_name = 'pokedex')
dex_raw = dex_raw.drop(["Unnamed: 15"], axis = 1)

list(dex_raw)
'''
    ['entryNo',
     'DexNo',
     'Pokemon',
     'Variation',
     'Form',
     'OriginalGame',
     'Location',
     'DateOfCapture',
     'Method',
     'Nickname',
     'Nature',
     'Ball',
     'Encounters',
     'Description',
     'user'] # change this to Trainer later, then learn to write to Excel with Pandas
'''

# Input Trainer Name to Sign in
user = "Fake-o Joe" # user = input("What is your name, Trainer?: ")

# Main Menu
    # View Stats / Data
    # View Pokemon Collection Details
    # Add New Pokemon 
    
## Add New Pokemon

    # take in inputs
    
entry = dex_raw['entryNo'].max() + 1 
No = 0 # *join with nat dex to auto look up this number)*
mon = 'Klefki' # input("Which shiny Pokemon did you catch?: ")
variat = []
form = []
og_game = []
loca = []
date_cap = []
meth = []
nickname = []
nature = []
ball = [] # ball = 
encounts = []
description = []
user = user

    # check if input is valid against table of Pokemon - error message after
    
dex_raw.loc[len(dex_raw)] = [entry, No, mon, variat, form, og_game, 
                           loca, date_cap, meth, nickname, nature, 
                           ball, encounts, description, user]
# GUI functionality to add:
    # search bar for Pokemon search



