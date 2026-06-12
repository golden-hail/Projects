# This code is generated using PyUIbuilder: https://pyuibuilder.com

import os
import tkinter as tk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


main = tk.Tk()
main.title("Main Window")
main.config(bg="#cf2b2b")
main.geometry("700x345")
main.update_idletasks()

geometryX = 0
geometryY = 0

main.geometry("+%d+%d"%(geometryX, geometryY))

menu = tk.Menu(main)
main.config(menu=menu)
menu_0 = tk.Menu(menu, tearoff=0)
menu_0.add_command(label="New", command=lambda: print("New clicked"))
menu_0.add_command(label="Open", command=lambda: print("Open clicked"))
menu.add_cascade(label="File", menu=menu_0)
menu_1 = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=menu_1)


main.mainloop()