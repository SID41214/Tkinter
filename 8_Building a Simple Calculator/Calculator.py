import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        label_result.config(text=f"Result: {result}")
    except Exception as e:
        label_result.config(text="Error!")

window = tk.Tk()
window.title("Simple Calculator")

# Entry widget
entry = tk.Entry(window, width=30)
entry.pack(pady=10)

# Button to calculate
btn = tk.Button(window, text="Calculate", command=calculate)
btn.pack(pady=5)

# Result Label
label_result = tk.Label(window, text="Result:")
label_result.pack(pady=5)

window.mainloop()
