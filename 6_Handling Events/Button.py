import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked!")

window = tk.Tk()
window.title("Event Handling")

# Label
label = tk.Label(window, text="Click the Button", font=("Arial", 14))
label.pack(pady=10)

# Button
button = tk.Button(window, text="Click Me", command=on_button_click)
button.pack(pady=10)

window.mainloop()
