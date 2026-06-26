import pandas as pd
import matplotlib.pyplot as plt

nat_dex = pd.read_excel('Shiny_Dex_og.xlsx', sheet_name = "pokedex")
dex_raw = pd.read_excel('Shiny_Dex_Out.xlsx', sheet_name = 'shiny_dex')

cols_2_drop = dex_raw.filter(regex=r'Unnamed:').columns
dex_raw = dex_raw.drop(columns=cols_2_drop)

'''
Shiny Pokemon Count Per Game
'''
## group pokemon count into OriginalGames for bar plot
game_mons = dex_raw.groupby("OriginalGame")["Pokemon"].agg("count").reset_index()

game_order = ['Yellow', 'Silver', 'Gold', 'Crystal', 'Ruby', 'Sapphire', 'Emerald', 
           'Fire Red', 'Leaf Green', 'Diamond', 'Pearl', 'Platinum', 'HeartGold', 'SoulSilver', 
           'Black', 'White', 'Black 2', 'White 2', 'X', 'Y', 'Alpha Sapphire', 'Omega Ruby',
           'Pokemon Go', 'Sun', 'Moon', 'Ultra Sun', 'Ultra Moon', "Let's Go Eevee", "Let's Go Pikachu", 
           'Sword', 'Shield', 'Brilliant Diamond', 'Shining Pearl', 'Legends of Arceus', 'Scarlet', 'Violet', 'Legends ZA']

total_mons = game_mons["Pokemon"].sum()
unique_mons = dex_raw['Pokemon'].nunique()

# Sort both lists based on the custom order index
sorted_pairs = sorted(zip(game_mons["OriginalGame"], game_mons["Pokemon"]), key=lambda x: game_order.index(x[0]))
game_order_sorted, mon_vals_sorted = zip(*sorted_pairs)

# Capture the BarContainer object, 
    #then automatically add labels to end of the bars

bars = plt.barh(game_order_sorted, mon_vals_sorted)
plt.bar_label(bars, padding=3)
plt.title("Shiny Pokemon Count Per Game")
plt.ylabel("Original Game")
plt.xlabel("Pokemon Count")

# --- ADDING THE TEXT BOX ---
ax = plt.gca() # Get current axes to handle positioning safely

box_style = dict(
    boxstyle='round,pad=0.5',
    facecolor='#f9f9f9',    # Clean light grey background
    edgecolor='#333333',    # Subtle dark grey border
    alpha=0.9
)

box_text = f"Total Caught: {total_mons}\nUnique Species: {unique_mons}"

# Coordinates (0.95, 0.92) place it near the top right, 
# slightly lowered so it doesn't collide with the title.
ax.text(0.95, 0.92, box_text, 
        transform=ax.transAxes, 
        fontsize=10,
        verticalalignment='top', 
        horizontalalignment='right', 
        bbox=box_style)
# ---------------------------

plt.tight_layout()
plt.show()

'''
Shiny Pokemon By Gender
'''
    # LOCate the entries where the Gender is set to "Female" for the following cols
f_tab = dex_raw.loc[dex_raw["Gender"] == "Female", ["Pokemon", "Gender", "OriginalGame"]]

f_game_counts = f_tab.groupby("OriginalGame")["Pokemon"].count().reset_index()

sorted_pairs = sorted(zip(f_game_counts["OriginalGame"], f_game_counts["Pokemon"]), key=lambda x: game_order.index(x[0]))
f_game_order, f_count = zip(*sorted_pairs)
    
    # THEN Males
m_tab = dex_raw.loc[dex_raw["Gender"] == "Male", ["Pokemon", "Gender", "OriginalGame"]]

m_game_counts = m_tab.groupby("OriginalGame")["Pokemon"].count().reset_index()  

sorted_pairs = sorted(zip(m_game_counts["OriginalGame"], m_game_counts["Pokemon"]), key=lambda x: game_order.index(x[0]))
m_game_order, m_count = zip(*sorted_pairs)

    # THEN No Gender 
ng_tab = dex_raw.loc[dex_raw["Gender"] == "No Gender",  ["Pokemon", "Gender", "OriginalGame"]]

ng_game_counts = ng_tab.groupby("OriginalGame")["Pokemon"].count().reset_index()

sorted_pairs = sorted(zip(ng_game_counts["OriginalGame"], ng_game_counts["Pokemon"]), key=lambda x: game_order.index(x[0]))
ng_game_order, ng_count = zip(*sorted_pairs)

    # THEN Unreported Genders
ug_tab = dex_raw.loc[(dex_raw["Gender"] != "Male") & (dex_raw["Gender"] != "Female") & (dex_raw["Gender"] != "No Gender"), ["Pokemon", "Gender", "OriginalGame"]]

ug_game_counts = ug_tab.groupby("OriginalGame")["Pokemon"].count().reset_index()

sorted_pairs = sorted(zip(ug_game_counts["OriginalGame"], ug_game_counts["Pokemon"]), key=lambda x: game_order.index(x[0]))
ug_game_order, ug_count = zip(*sorted_pairs)

# Plot the genders per game (make side by side instead of transparent 
# so I can keep the number labels)
bars = plt.bar(f_game_order, f_count, color = 'm', alpha = 0.6, label = "Female")
bars = plt.bar(m_game_order, m_count, color = 'b', alpha = 0.6, label = "Male")
bars = plt.bar(ng_game_order, ng_count, color = 'c', alpha = 0.6, label = "No Gender")
# bars = plt.bar(ug_game_order, ug_count, color = 'c', alpha = 0.6, label = "Unreported Gender")
# create box with unreported gender count
plt.xlabel("Originating Game")
plt.ylabel("Number of Female Shinies")
plt.title("Shiny Count by Gender")
plt.legend()
plt.xticks(rotation=50)
plt.tight_layout()
plt.show()

##

# 1. Standardize 'Unreported Gender' names so they don't break out into multiple categories
# We define our known genders, anything else becomes 'Unreported Gender'
known_genders = ['Female', 'Male', 'No Gender']
plot_df = dex_raw.copy()
plot_df.loc[~plot_df['Gender'].isin(known_genders), 'Gender'] = 'Unreported Gender'

# 2. Use pivot_table/crosstab to automatically align games and genders into a single grid
# This guarantees that every gender has an exact matching list of games (even if count is 0)
gender_counts = pd.crosstab(plot_df['OriginalGame'], plot_df['Gender'])

# 3. Reindex to match your exact 'game_order' list safely
# (Only includes games that actually exist in your list to prevent errors)
available_games = [game for game in game_order if game in gender_counts.index]
gender_counts = gender_counts.reindex(available_games)

# 4. Plot side-by-side grouped bars using pandas wrapper (super stable)
# 'width=0.8' spreads the 4 grouped bars nicely across each game slot
ax = gender_counts.plot(kind='bar', figsize=(12, 6), width=0.8,
                        color=['#d63384', '#0d6efd', '#20c997', '#6c757d'], alpha=0.85)

# 5. Add bar labels to EVERY category dynamically
for container in ax.containers:
    # Optional: labels= to hide '0' labels so the chart stays clean
    labels = [f'{int(v):,}' if v > 0 else '' for v in container.datavalues]
    ax.bar_label(container, labels=labels, padding=3, fontsize=8)

# 6. Styling
plt.title("Shiny Count by Gender Per Game", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Originating Game", fontweight='bold', labelpad=10)
plt.ylabel("Pokemon Count", fontweight='bold', labelpad=10)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.legend(frameon=True)

plt.tight_layout()
plt.show()

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

no_vari_join = pd.merge(no_vari, nat_dex, how = "inner", on = "Pokemon")

# Drop the non-variation dupe with the "latest" Region...
    # will need to prescribe this order                                                                                                    
region_order = ['Kanto', 'Johto', 'Hoenn', 'Sinnoh', 'Unova', 'Kalos', 'Alola', 'Galar', 'Hisui', 'Paldea', 'Unknown']
                  
no_vari_join['Region'] = pd.Categorical(no_vari_join['Region'], categories=region_order, ordered=True)  
no_vari_join = no_vari_join.sort_values('Region')
dupe_subset = ['Pokemon']
no_vari_join = no_vari_join.drop_duplicates(subset=dupe_subset, keep ='first')

mon_data = pd.concat([no_vari_join, cap_vari_join])

a = dex_raw[dex_raw.duplicated(subset = ["DexNo", "Variation"])] # the ndon't forget about teh varients!@

## plot by Pokemon types (two columns)

'''
Shiny Pokemon Capture Dates
'''
## plot by date
    # get values with valid date time
    # what to do with other columns with no date time listed?? info box in corner
    # avg per year 
    # yearly summary
    # average per year, per game
## Am I a lucky trainer? (need encounter based data)
# avg encounters? need to goog data it and investigate and update entries
    # should also account for different odds in different games
# normal distribution?
# hypothesis test, don't count 
# add odds to meta data

###########
#SNIPPITS
###########
# clean up snippet from a Soulsilver entry above ()
# row_index = dex_raw.loc[dex_raw["OriginalGame"] == "Soulsilver"].index[0]
# dex_raw.loc[dex_raw["OriginalGame"] == "Soulsilver", 'OriginalGame'] = "SoulSilver"

## dex_raw.to_excel('Shiny_Dex_Out.xlsx', sheet_name = 'shiny_dex')