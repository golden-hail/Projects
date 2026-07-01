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
plt.xlim(0, max(mon_vals_sorted) + 17)

# --- ADDING THE TEXT BOX ---
ax = plt.gca() # Get current axes to handle positioning safely

box_style = dict(
    boxstyle='round,pad=0.5',
    facecolor='#f9f9f9',    
    edgecolor='#333333',    
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
