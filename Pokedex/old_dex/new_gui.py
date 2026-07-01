'''
url: 
https://medium.com/@jsw.tan1991/the-pokedex-introduction-to-guis-with-tkinter-15f6b0e88c76
'''

import tkinter as tk

# The window!
window = tk.Tk()

window.title("Pokedex")
window.geometry("800x500")
window.configure(background = "crimson")

# Configure 4 rows and 3 columns.
window.rowconfigure([i for i in range(4)], minsize = 50, weight = 1)
window.columnconfigure([i for i in range(3)], minsize = 50, weight = 1)

### Name Frame
name_frame = tk.Frame(window, relief = tk.RAISED, borderwidth = 4)
label = tk.Label(name_frame, text = "Pokemon Name Here", font = ("Futura", 16))
# One of the few cases where you can mix pack() with grid().
label.pack()
name_frame.grid(row = 0, column = 0)

### Picture Frame
picture_frame = tk.Frame(window, relief = tk.SUNKEN, borderwidth = 2)
label = tk.Label(picture_frame, text = "Pokemon Picture Here", font = ("Futura", 16))
label.pack()
picture_frame.grid(row = 1, column = 0, rowspan = 2, sticky = "ns")

### Type Frame
type_frame = tk.Frame(window, relief = tk.RAISED, borderwidth = 2)
type1label = tk.Label(type_frame, text = "Type 1 Here", font = ("Futura", 12))
type1label.grid(row = 0, column = 0)
type2label = tk.Label(type_frame, text = "Type 2 Here", font = ("Futura", 12))
type2label.grid(row = 0, column = 1)
type_frame.grid(row = 3, column = 0)

### Search Frame
search_frame = tk.Frame(window, relief = tk.RAISED, borderwidth = 2)

# Calling rowconfigure and columnfigure within the info_frame
# causes the contents of the frame (label) to be centered within it.
search_frame.columnconfigure([0,1,2,3], weight = 1)

label = tk.Label(search_frame, text = "Left Arrow", font = ("Futura", 16))
label.grid(row = 0, column = 0)

label = tk.Label(search_frame, text = "Search Box\nwith Drop-down Menu?", font = ("Futura", 16))
label.grid(row = 0, column = 1, columnspan = 2)

label = tk.Label(search_frame, text = "Right Arrow", font = ("Futura", 16))
label.grid(row = 0, column = 3)

search_frame.grid(row = 0, column = 1, columnspan = 2, sticky = "ew")

### Info Frame
info_frame = tk.Frame(window, relief = tk.SUNKEN, borderwidth = 4)

# Calling rowconfigure and columnfigure within the info_frame
# causes the contents of the frame (label) to be centered within it.
info_frame.rowconfigure([0,1,2], weight = 1)
info_frame.columnconfigure([0,1], weight = 1)

## Various Information

# The Pokedex entry is long, so we'll let it take up two columns
pokedex_entry = tk.Label(info_frame, text = "Pokedex Entry", font = ("Futura", 16))
pokedex_entry.grid(row = 0, column = 0, columnspan = 2)

height_entry = tk.Label(info_frame, text = "Height", font = ("Futura", 16))
height_entry.grid(row = 1, column = 0)

weight_entry = tk.Label(info_frame, text = "Weight", font = ("Futura", 16))
weight_entry.grid(row = 1, column = 1)

species_entry = tk.Label(info_frame, text = "Species", font = ("Futura", 16))
species_entry.grid(row = 2, column = 0)

catch_entry = tk.Label(info_frame, text = "Catch Rate", font = ("Futura", 16))
catch_entry.grid(row = 2, column = 1)

info_frame.grid(row = 1, rowspan = 3, column = 1, columnspan = 2, sticky = "nsew")

# Run the App
window.mainloop()