'''
Shiny Pokemon by Types
'''

import pandas as pd
import matplotlib.pyplot as plt

nat_dex = pd.read_excel('Shiny_Dex_og.xlsx', sheet_name = "pokedex")
dex_raw = pd.read_excel('Shiny_Dex_Out.xlsx', sheet_name = 'shiny_dex')

cols_2_drop = dex_raw.filter(regex=r'Unnamed:').columns
dex_raw = dex_raw.drop(columns=cols_2_drop)

# Change dex_raw[Variation] to match the nat_dex[Region] values 
dex_raw["Variation"] = dex_raw["Variation"].replace({'Alolan' : 'Alola',
                            'Galarian' : 'Galar',
                            'Hisuin' : 'Hisui',
                            'Paldean' : 'Paldea'})

# Join nat_dex data into dex_raw to get shiny mon meta info (copy clones the data in memory)
cap_mons_vari = dex_raw[dex_raw["Variation"].notna()].copy()

    # Clean trailing spaces before merge 
cap_mons_vari['Pokemon'] = cap_mons_vari['Pokemon'].astype(str).str.strip()
cap_mons_vari['Variation'] = cap_mons_vari['Variation'].astype(str).str.strip()

nat_dex['Pokemon'] = nat_dex['Pokemon'].astype(str).str.strip()
nat_dex['Region'] = nat_dex['Region'].astype(str).str.strip()

cap_vari_join = pd.merge(cap_mons_vari, nat_dex, how = "left", left_on = ["Pokemon", "Variation"], right_on = ["Pokemon", "Region"])

# Join nat_dex to dex_raw for non-variation Pokemon
no_vari = dex_raw[dex_raw["Variation"].isna()].copy()

    # Clean trailing spaces before merge 
no_vari['Pokemon'] = no_vari['Pokemon'].astype(str).str.strip()
no_vari['Variation'] = no_vari['Variation'].astype(str).str.strip()

# Map each region in the region_order to a numeric rank in the nat_dex
region_order = ['Kanto', 'Johto', 'Hoenn', 'Sinnoh', 'Unova', 'Kalos', 'Alola', 'Galar', 'Hisui', 'Paldea', 'Unknown']

region_rank_map = {region: i for i, region in enumerate(region_order)}
nat_dex["Rank"] = nat_dex["Region"].map(region_rank_map)

# find the "best ranking" (original, nonvariation form Pokemon)
nat_dex["Best_Rank"] = nat_dex.groupby("Pokemon")["Rank"].transform("min")

cleaned_df = nat_dex[nat_dex["Rank"] == nat_dex["Best_Rank"]]

# drop all variations/ unoriginal regions of Pokemon from the national dex to ease merge
nat_dex = cleaned_df.drop(columns=["Rank", "Best_Rank"])

no_vari_join = pd.merge(no_vari, nat_dex, how = "left", on = "Pokemon")

# Bring Variation and Non-Variation mons back together for analysis
mon_data = pd.concat([no_vari_join, cap_vari_join])

# Only keep entries in DataFrame that have a Type 1 associated to them
mon_data = mon_data.loc[mon_data["Type 1"].notna()]

## plot by Pokemon types (two columns)
pos_types = ['Water', 'Steel', 'Grass', 'Dragon', 'Ghost', 'Dark', 'Fire',
       'Psychic', 'Ground', 'Poison', 'Bug', 'Electric', 'Normal',
       'Fighting', 'Rock', 'Fairy', 'Ice', 'Flying']

type_1 = mon_data["Type 1"].value_counts()
type_2 = mon_data["Type 2"].value_counts()

type_counts = type_1.add(type_2, fill_value = 0)
type_counts = type_counts.drop('-')
type_counts = type_counts.reset_index

plt.tight_layout()
plt.savefig(fname = "plot_Shinies_Types.png")
plt.bar()



