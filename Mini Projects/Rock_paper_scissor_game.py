# Create a simple Rock, Paper, Scissors game 
# where a user plays against the computer.

import tkinter as tk
import random

def play(choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    result = ""
    if choice == computer_choice:
        result = "It's a Tie!"
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Scissors" and computer_choice == "Paper") or \
         (choice == "Paper" and computer_choice == "Rock"):
        result = "You Win!"
    else:
        result = "You Lose!"
    label_result.config(text=f"Computer: {computer_choice}\n{result}")

window = tk.Tk()
window.title("Rock, Paper, Scissors")

label = tk.Label(window, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14))
label.pack(pady=10)

frame = tk.Frame(window)
frame.pack()

btn_rock = tk.Button(frame, text="Rock", command=lambda: play("Rock"))
btn_rock.pack(side=tk.LEFT, padx=10)

btn_paper = tk.Button(frame, text="Paper", command=lambda: play("Paper"))
btn_paper.pack(side=tk.LEFT, padx=10)

btn_scissors = tk.Button(frame, text="Scissors", command=lambda: play("Scissors"))
btn_scissors.pack(side=tk.LEFT, padx=10)

label_result = tk.Label(window, text="", font=("Arial", 14))
label_result.pack(pady=10)

window.mainloop()
