import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Information", "Hello! This is a message.")

window = tk.Tk()
window.title("Messagebox Example")

# Button to show a messagebox
btn = tk.Button(window, text="Show Message", command=show_message)
btn.pack(pady=20)

window.mainloop()
