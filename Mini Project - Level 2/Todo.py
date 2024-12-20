# Todo List Application
# Description: A simple To-Do list where users can add and delete tasks.

# Features:

# Add tasks via an input field.
# Display tasks in a listbox.
# Remove tasks by selecting them.

import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)
    else:
        messagebox.showwarning("Warning", "No task selected!")

root = tk.Tk()
root.title("Todo List")

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

root.mainloop()
