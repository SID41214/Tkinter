# Create a simple calculator that performs basic arithmetic operations like 
# addition, subtraction, multiplication, and division.

import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        label_result.config(text=f"Result: {result}")
    except Exception as e:
        label_result.config(text="Error!")

window = tk.Tk()
window.title("Calculator")

entry = tk.Entry(window, width=20)
entry.pack(pady=10)

btn = tk.Button(window, text="Calculate", command=calculate)
btn.pack(pady=10)

label_result = tk.Label(window, text="Result: ")
label_result.pack(pady=10)

window.mainloop()
