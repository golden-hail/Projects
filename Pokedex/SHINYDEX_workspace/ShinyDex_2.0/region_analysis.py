import pandas as pd

nat_dex = pd.read_excel('Shiny_Dex_og.xlsx', sheet_name = "pokedex")
dex_raw = pd.read_excel('Shiny_Dex.xlsx', sheet_name = 'shiny_dex')
# drop bad columns
cols_2_drop = dex_raw.filter(regex=r'Unnamed:').columns
dex_raw = dex_raw.drop(columns=cols_2_drop)

list(nat_dex)

mon_vari = dex_raw[["Pokemon", "Variation", "OriginalGame"]]

# plot by region
# plot by date
# avg encounters? need to goog data it and investigate and update entries
# normal distribution?
# hypothesis test
# add odds to meta data


