import tkinter as tk
from tkinter import messagebox
import os

TASKS_FILE = "tasks.txt"

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty.")

def delete_task():
    try:
        selected = listbox.curselection()
        listbox.delete(selected)
    except:
        messagebox.showwarning("Select Error", "Please select a task to delete.")

def save_tasks():
    with open(TASKS_FILE, "w") as file:
        tasks = listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Saved", "Tasks saved successfully!")

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            for line in file:
                listbox.insert(tk.END, line.strip())

# GUI setup
root = tk.Tk()
root.title("To-Do List App")

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=30)
entry.grid(row=0, column=0, padx=10)

add_btn = tk.Button(frame, text="Add Task", command=add_task)
add_btn.grid(row=0, column=1)

listbox = tk.Listbox(root, width=45, height=10)
listbox.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

delete_btn = tk.Button(btn_frame, text="Delete Task", command=delete_task)
delete_btn.grid(row=0, column=0, padx=5)

save_btn = tk.Button(btn_frame, text="Save Tasks", command=save_tasks)
save_btn.grid(row=0, column=1, padx=5)

load_btn = tk.Button(btn_frame, text="Load Tasks", command=load_tasks)
load_btn.grid(row=0, column=2, padx=5)

# Load tasks on start
load_tasks()

root.mainloop()
