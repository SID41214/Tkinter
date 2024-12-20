# Description: A basic calculator application that can perform addition, subtraction, multiplication, and division.

# Features:

# Input fields for numbers.
# Buttons for operations.
# A display for results.
import tkinter as tk

def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(expression)
            screen_var.set(result)
            expression = str(result)
        except Exception:
            screen_var.set("Error")
            expression = ""
    elif text == "C":
        expression = ""
        screen_var.set(expression)
    else:
        expression += text
        screen_var.set(expression)

root = tk.Tk()
root.title("Calculator")

expression = ""
screen_var = tk.StringVar()

screen = tk.Entry(root, textvar=screen_var, font="Arial 20 bold", bd=8, relief=tk.SUNKEN, justify=tk.RIGHT)
screen.pack(fill=tk.BOTH, padx=10, pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/"
]

row, col = 0, 0
for button in buttons:
    btn = tk.Button(button_frame, text=button, font="Arial 15 bold", width=5, height=2)
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", click)
    col += 1
    if col > 3:
        row += 1
        col = 0

root.mainloop()
