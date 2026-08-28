'''
Shiny Pokemon Capture Dates
'''

import pandas as pd
import matplotlib.pyplot as plt

nat_dex = pd.read_excel('Shiny_Dex_og.xlsx', sheet_name = "pokedex")
dex_raw = pd.read_excel('Shiny_Dex_Out.xlsx', sheet_name = 'shiny_dex')

cols_2_drop = dex_raw.filter(regex=r'Unnamed:').columns
dex_raw = dex_raw.drop(columns=cols_2_drop)

import datetime

# Find entries in the DateOfCapture column that are not datetime formatted
dex_raw['DateOfCapture'] = pd.to_datetime(dex_raw['DateOfCapture'], errors='coerce')

# Remove data where NAT is listed
NaT_date = dex_raw[dex_raw['DateOfCapture'].isna()]
dex = dex_raw[dex_raw['DateOfCapture'].notna()]

dex = dex.sort_values("DateOfCapture")


'''
Shiny Pokemon per year 
'''

shiny_per_year = dex.groupby(dex['DateOfCapture'].dt.year)['Pokemon'].count().reset_index()

bars = plt.bar(shiny_per_year["DateOfCapture"], shiny_per_year["Pokemon"])
plt.bar_label(bars)
plt.xlabel("Year")
plt.ylabel("# of Pokemon")
plt.ylim(0.5, max(shiny_per_year["Pokemon"])+5)
plt.title("Shiny Pokemon by Year")

# Unlisted Mons
ax = plt.gca() # Get current axes to handle positioning safely

box_style = dict(
    boxstyle='round,pad=0.5',
    facecolor='#f9f9f9',    
    edgecolor='#333333',    
    alpha=0.9
)

box_text = f"Unreported: {len(NaT_date)}"

# Coordinates (0.95, 0.92) place it near the top right, 
# slightly lowered so it doesn't collide with the title.
ax.text(0.25, 0.92, box_text, 
        transform=ax.transAxes, 
        fontsize=10,
        verticalalignment='top', 
        horizontalalignment='right', 
        bbox=box_style)
# ---------------------------
plt.tight_layout()
plt.savefig(fname = "Shinies_per_Year.png")
plt.show()

# When I work on my GUI, I will be able to filter on date ranges which will make this 
    # plot much more valuable and legible 

## Am I a lucky trainer? (need encounter based data)
# avg encounters? need to goog data it and investigate and update entries
    # should also account for different odds in different games
# normal distribution?
# hypothesis test, don't count 
# add odds to meta data