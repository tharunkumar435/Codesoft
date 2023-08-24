import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def edit_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_index)
        entry_task.delete(0, tk.END)
        entry_task.insert(tk.END, task)
        listbox_tasks.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to edit.")

def save_tasks():
    with open("tasks.txt", "w") as file:
        tasks = listbox_tasks.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                listbox_tasks.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

root = tk.Tk()
root.title("To-Do List")

frame_input = tk.Frame(root)
frame_input.pack(pady=10)

entry_task = tk.Entry(frame_input, width=50)
entry_task.pack(side=tk.LEFT, padx=5)

button_add_task = tk.Button(frame_input, text="Add Task", command=add_task)
button_add_task.pack(side=tk.LEFT, padx=5)

frame_tasks = tk.Frame(root)
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, width=50, height=10)
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=5)

button_delete_task = tk.Button(frame_buttons, text="Delete Task", command=delete_task)
button_delete_task.pack(side=tk.LEFT, padx=5)

button_edit_task = tk.Button(frame_buttons, text="Edit Task", command=edit_task)
button_edit_task.pack(side=tk.LEFT, padx=5)

button_save_tasks = tk.Button(root, text="Save Tasks", command=save_tasks)
button_save_tasks.pack(pady=5)

load_tasks()

root.mainloop()
