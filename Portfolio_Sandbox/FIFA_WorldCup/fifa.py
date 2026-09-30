'''
Which country has won the most World Cup matches?
Which World Cup had the highest number of goals?
Which stadium hosted the most matches?
How many matches went to penalties?
How have scoring trends changed over time?
'''

import pandas as pd

fifa_data = pd.read_csv('wcplayerstatistics2026.csv')

# Check for non-ASCII characters in Player, Squad, and Club - 
#Note: unicodedata is standard to import it when working on encoding tasks (ex: stripping accents).
import unicodedata

def has_non_ascii(text):
    if not isinstance(text, str):
        return False
    return any(ord(char) > 127 for char in text)

non_ascii_players = fifa_data[fifa_data['Player'].apply(has_non_ascii)]

# print(f"Number of players with non-ASCII characters: {len(non_ascii_players)}")
# print("\nSample non-ASCII player names:")
# print(non_ascii_players[['Player', 'Squad', 'Club']].head(10))

# Demonstrate unidecode / unicodedata normalization

def remove_accents(text):
    if not isinstance(text, str):
        return text
    # Normalize unicode characters to NFKD decomposed form, then drop non-spacing mark combining characters
    return ''.join(c for c in unicodedata.normalize('NFKD', text) if unicodedata.category(c) != 'Mn')

# Test on sample

# for each column, remove the accents
non_ascii_players_copy = non_ascii_players.copy()
non_ascii_players_copy['Player_ASCII'] = non_ascii_players_copy['Player'].apply(remove_accents)

print(non_ascii_players_copy[['Player', 'Player_ASCII']].head(10))



### try unicode for turkish letters??

# Using unidecode for Turkish characters like 'ı' or 'ş'
# try:
#     from unidecode import unidecode
#     non_ascii_players_copy['Player_Unidecode'] = non_ascii_players_copy['Player'].apply(unidecode)
#     print("Unidecode sample:")
#     print(non_ascii_players_copy[['Player', 'Player_ASCII', 'Player_Unidecode']].iloc[8:12])
# except ImportError:
#     print("unidecode not installed, using custom map or fallback")

# step one, look for ascii to replace in all columns.



