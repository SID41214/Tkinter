# Adding Widgets (Labels, Buttons, Entry and Text)

import tkinter as tk

window = tk.Tk()
window.title("Widgets")
window.geometry("400x400")

# Adding label widget
label= tk.Label(window, text="HEllooooooooo", font=("Arial",25),fg="blue")
label.pack(pady=10)  #Adding padding

# Add an Entry widget (Textbox)
entry = tk.Entry(window, width=30)
entry.pack(pady=10)

# Add a Button widget
def on_button_click():
    user_input = entry.get()
    label.config(text=f"Hello, {user_input}!")

button = tk.Button(window, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Add a Text widget (Multi-line text box)
# text = tk.Text(window, height=5, width=40)
# text.pack(pady=10)

window.mainloop()
