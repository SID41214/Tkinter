import tkinter as tk

window = tk.Tk()
window.title("Frames Example")
window.geometry("400x300")

# Create Frames
top_frame = tk.Frame(window, bg="lightgray")
top_frame.pack(fill="x", pady=5)

bottom_frame = tk.Frame(window, bg="lightblue")
bottom_frame.pack(fill="both", expand=True)

# Add widgets to top frame
btn1 = tk.Button(top_frame, text="Button 1", fg="red")
btn1.pack(side="left", padx=5)

btn2 = tk.Button(top_frame, text="Button 2", fg="green")
btn2.pack(side="left", padx=5)

# Add widgets to bottom frame
label = tk.Label(bottom_frame, text="This is the Bottom Frame", font=("Arial", 12))
label.pack(pady=20)

window.mainloop()
