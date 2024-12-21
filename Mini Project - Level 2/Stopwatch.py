# Description: A stopwatch with start, stop, and reset functionalities.

# Features:

# Start, stop, and reset buttons.
# Time display in minutes and seconds.
import tkinter as tk

# Global variables
counter = 0
running = False

def start_timer():
    """Start the stopwatch."""
    global running
    if not running:
        running = True
        update_time()

def stop_timer():
    """Stop the stopwatch."""
    global running
    running = False

def reset_timer():
    """Reset the stopwatch."""
    global counter, running
    running = False
    counter = 0
    time_label.config(text="00:00:00")  # Reset display to zero

def update_time():
    """Update the timer display."""
    global counter
    if running:
        minutes, seconds = divmod(counter, 60)
        hours, minutes = divmod(minutes, 60)
        time_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
        counter += 1
        # Schedule the next update after 1000 ms (1 second)
        root.after(1000, update_time)

# Tkinter GUI setup
root = tk.Tk()
root.title("Stopwatch")

time_label = tk.Label(root, text="00:00:00", font=("Arial", 30), bg="black", fg="white")
time_label.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

start_button = tk.Button(button_frame, text="Start", command=start_timer, font=("Arial", 12), width=10)
start_button.grid(row=0, column=0, padx=5)

stop_button = tk.Button(button_frame, text="Stop", command=stop_timer, font=("Arial", 12), width=10)
stop_button.grid(row=0, column=1, padx=5)

reset_button = tk.Button(button_frame, text="Reset", command=reset_timer, font=("Arial", 12), width=10)
reset_button.grid(row=0, column=2, padx=5)

root.mainloop()
