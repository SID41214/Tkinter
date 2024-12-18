# Using Grid for Precise Layouts
# The Grid geometry manager allows you to 
# place widgets in a table format.

import tkinter as tk

window = tk.Tk()
window.title("Grid Example")
window.geometry("300x200")

# Add widgets using grid
label1 = tk.Label(window, text="Name:")
label1.grid(row=0, column=0, padx=5, pady=5)

entry1 = tk.Entry(window)
entry1.grid(row=0, column=1, padx=5, pady=5)

label2 = tk.Label(window, text="Age:")
label2.grid(row=1, column=0, padx=5, pady=5)

entry2 = tk.Entry(window)
entry2.grid(row=1, column=1, padx=5, pady=5)

btn = tk.Button(window, text="Submit")
btn.grid(row=2, column=0, columnspan=2, pady=10)

window.mainloop()
