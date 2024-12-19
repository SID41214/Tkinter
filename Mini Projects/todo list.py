# Create a to-do list where users can add tasks, delete tasks, and clear all tasks.

import tkinter as tk

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        pass

def clear_tasks():
    listbox.delete(0, tk.END)

window = tk.Tk()
window.title("To-Do List")

entry = tk.Entry(window, width=30)
entry.pack(pady=10)

btn_add = tk.Button(window, text="Add Task", command=add_task)
btn_add.pack(pady=5)

btn_delete = tk.Button(window, text="Delete Task", command=delete_task)
btn_delete.pack(pady=5)

btn_clear = tk.Button(window, text="Clear All", command=clear_tasks)
btn_clear.pack(pady=5)

listbox = tk.Listbox(window, width=30, height=10)
listbox.pack(pady=10)

window.mainloop()
