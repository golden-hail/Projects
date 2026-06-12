# import tkinter as tk
# from tkinter import messagebox

# def say_hello():
#     messagebox.showinfo("Greeting", f"Hello, {entry.get()}!")

# # 1. Create main application window
# root = tk.Tk()
# root.title("Free Python GUI")
# root.geometry("300x150")

# # 2. Add text instruction
# label = tk.Text = tk.Label(root, text="Enter your name:")
# label.pack(pady=5)

# # 3. Add a text entry field
# entry = tk.Entry(root)
# entry.pack(pady=5)

# # 4. Add a clickable button
# button = tk.Button(root, text="Submit", command=say_hello)
# button.pack(pady=5)

# # 5. Start the application loop
# root.mainloop()

import tkinter as tk
from tkinter import ttk

def show_selection():
    # Use .get() to retrieve the currently selected text
    selected_value = combo.get()
    label.config(text=f"Selected: {selected_value}")

# Initialize main window
root = tk.Tk()
root.title("Shiny Catch Details")
root.geometry("300x200")

# Define the choices of Pokeball
ball_options = ["Poke Ball", "Great Ball", "Ultra Ball", "Master Ball", 
                "Safari Ball", "Sport Ball", "Premier Ball", "Cherish Ball",
                "Park Ball", "Beast Ball", "Origin Ball", "Net Ball", "Dive Ball",
                "Nest Ball", "Repeat Ball", "Timer Ball", "Luxury Ball", "Heal Ball",
                "Quick Ball", "Dusk Ball", "Dream Ball", "Fast Ball", "Heavy Ball",
                "Level Ball", "Love Ball", "Moon Ball", "Lure Ball", "Feather Ball",
                "Wing Ball", "Jet Ball", "Heavy Ball", "Leaden Ball", "Gigaton Ball"]

ball_options.sort()

# Create the Combobox
combo = ttk.Combobox(root, values=ball_options, state="readonly")
combo.set("Select a Pokeball") 
combo.pack(pady=20)

# Create a button to trigger action
button = tk.Button(root, text="Submit", command=show_selection)
button.pack(pady=5)

# Create a label to display output
label = tk.Label(root, text="")
label.pack(pady=10)

root.mainloop()