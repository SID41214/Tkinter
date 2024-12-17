import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Hello Tkinter")
root.geometry("300x200")  # Set window size (width x height)

# Add a Label widget
label = tk.Label(root, text="Welcome to Tkinter!", font=("Arial", 14))
label.pack(pady=20)  # Add some padding

# Run the application
root.mainloop()
