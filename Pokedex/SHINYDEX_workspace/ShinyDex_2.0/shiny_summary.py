import pandas as pd
import datetime

dex_raw = pd.read_excel('Shiny_Dex_Out.xlsx', sheet_name = "shiny_dex")
nat_dex = pd.read_excel('Shiny_Dex_og.xlsx', sheet_name = "pokedex")

cols_2_drop = dex_raw.filter(regex=r'Unnamed:').columns
dex_raw = dex_raw.drop(columns=cols_2_drop)

### Mons count per game
game_order = ['Yellow', 'Silver', 'Gold', 'Crystal', 'Ruby', 'Sapphire', 'Emerald', 
           'Fire Red', 'Leaf Green', 'Diamond', 'Pearl', 'Platinum', 'HeartGold', 'SoulSilver', 
           'Black', 'White', 'Black 2', 'White 2', 'X', 'Y', 'Alpha Sapphire', 'Omega Ruby',
           'Pokemon Go', 'Sun', 'Moon', 'Ultra Sun', 'Ultra Moon', "Let's Go Eevee", "Let's Go Pikachu", 
           'Sword', 'Shield', 'Brilliant Diamond', 'Shining Pearl', 'Legends of Arceus', 'Scarlet', 'Violet', 'Legends ZA']

game_counts = dex_raw['OriginalGame'].value_counts()

### Count per year
dex_raw['DateOfCapture'] = pd.to_datetime(dex_raw['DateOfCapture'])
dex = dex_raw.dropna(subset = ['DateOfCapture'])

year_count = dex.groupby(dex['DateOfCapture'].dt.year)['Pokemon'].count()

### % of each region  (something is wrong here...)
dex_raw['Variation'] = dex_raw['Variation'].replace('Galarian', 'Galar').replace('Alolan', 'Alola').replace('Hisuin', 'Hisui').replace('Paldean', 'Paldea')

# fill the national dex with shiny dex entries
merge_dex = pd.merge(nat_dex, dex_raw, how = 'left', left_on = 'NdexNo', right_on = 'DexNo')

# Weed through duplicate mons - Pokemon such as Meowth have different forms, such as original, Galarian, and Alolan. 
    # Since we left merged on dex number, the new dataframe created duplicates of each Pokemon_x with different region/variations

# Get National dex entries for non dexed shiny mons
empty_entry = merge_dex[merge_dex['entryNo'].isna()]

# Find the duplicate shiny Pokemon entries to determine which entries match the national dex
dupe_mons = merge_dex[merge_dex.duplicated(subset='Pokemon_x', keep=False)]
dupe_entries = dupe_mons[dupe_mons['entryNo'].notna()]

# Use boolean indexing to see if Region and Variation match. If they do, that's a good entry.
# if not, we asess the entries further, but drop the matches
var_match = dupe_entries[dupe_entries['Region'] == dupe_entries['Variation']].copy()
remaining_dupes = dupe_entries[dupe_entries['Region'] != dupe_entries['Variation']].copy()

# Since we handled all the entries of mons with variations, we can drop the non-nan Variation rows
# then drop the Regions that we checked Variations across
rem_dupes = remaining_dupes[remaining_dupes['Variation'].isna()]

no_dupes = rem_dupes[~rem_dupes['Region'].isin(['Alola', 'Galar', 'Hisui', 'Paldea'])]
    # boolean way: rem_dupes = rem_dupes[(rem_dupes['Region'] != 'Alola') & (rem_dupes['Region'] != 'Galar')]

# Append cleaned data back together
total_dex = pd.concat([empty_entry, var_match, no_dupes], ignore_index = True)

# total shiny dex %

# type counts 

## Expand Later (Reach Goals)
# gender count per game
# most active hunting seasons
# shinies by types 
# lucky rates per game? (standarize data? need more Pokemon Go data)
