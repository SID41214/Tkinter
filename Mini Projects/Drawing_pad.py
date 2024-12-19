# Create a drawing pad where users can draw by clicking and dragging the mouse.

import tkinter as tk

def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x-2, y-2, x+2, y+2, fill="black")

window = tk.Tk()
window.title("Drawing Pad")

canvas = tk.Canvas(window, width=500, height=500, bg="white")
canvas.pack()

canvas.bind("<B1-Motion>", draw)

window.mainloop()
