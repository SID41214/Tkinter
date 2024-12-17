import tkinter as tk

# Create the main window
window = tk.Tk()
windoow.title("Hello Tkinter")
window.geometry("300x200")  # Set window size (width x height)

# Add a Label widget
label = tk.Label(window, text="Welcome to Tkinter!", font=("Arial", 14))
label.pack(pady=20)  # Add some padding

# Run the application
window.mainloop()
