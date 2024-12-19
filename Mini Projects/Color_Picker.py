# Create a color picker where users can choose a color, and the background changes to the selected color

import tkinter as tk
from tkinter import colorchooser

def pick_color():
    color_code = colorchooser.askcolor(title="Choose Color")[1]
    if color_code:
        window.config(bg=color_code)

window = tk.Tk()
window.title("Color Picker")

btn = tk.Button(window, text="Pick a Color", command=pick_color)
btn.pack(pady=20)

window.mainloop()
