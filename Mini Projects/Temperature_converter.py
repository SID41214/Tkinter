# Create a temperature converter that converts temperatures between Celsius and Fahrenheit.

import tkinter as tk

def convert():
    try:
        celsius = float(entry.get())
        fahrenheit = (celsius * 9/5) + 32
        label_result.config(text=f"{celsius}°C = {fahrenheit:.2f}°F")
    except ValueError:
        label_result.config(text="Invalid Input!")

window = tk.Tk()
window.title("Temperature Converter")

label = tk.Label(window, text="Enter temperature in Celsius:", font=("Arial", 14))
label.pack(pady=10)

entry = tk.Entry(window, width=20)
entry.pack(pady=10)

btn = tk.Button(window, text="Convert", command=convert)
btn.pack(pady=10)

label_result = tk.Label(window, text="", font=("Arial", 14))
label_result.pack(pady=10)

window.mainloop()
