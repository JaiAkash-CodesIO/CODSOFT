import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("400x400")
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)
def delete_task():
    try:
        task_listbox.delete(tk.ANCHOR)
    except:
        messagebox.showwarning("Warning", "You must select a task.")
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)
def complete_task():
    try:
        task_index = task_listbox.curselection()[0]
        task = task_listbox.get(task_index)
        task_listbox.delete(task_index)
        task_listbox.insert(tk.END, task + " (Completed)")
    except:
        messagebox.showwarning("Warning", "You must select a task.")
complete_button = tk.Button(root, text="Complete Task", command=complete_task)
complete_button.pack(pady=5)
import json
def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
            for task in tasks:
                task_listbox.insert(tk.END, task)
    except FileNotFoundError:
        pass
def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)
load_tasks()
root.protocol("WM_DELETE_WINDOW", save_tasks)
root.mainloop()
