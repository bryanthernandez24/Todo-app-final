
from tkinter import Frame, Listbox,END
from tkinter import ttk
from tkinter import messagebox
from typing import List

from taskItem import TaskItem


class ToDoList(Frame):
    def __init__(self, parent,controller):
        super().__init__(parent)
        self.controller = controller

        # List to store tasks
        self.task_listbox = None
        self.add_task_btn = None
        self.task_entry = None
        self.delete_task_btn = None
        self.tasks:List[TaskItem] = []
        
        # Create widgets
        self.create_widgets()
        
    def create_widgets(self):
        # Entry for new task
        self.task_entry = ttk.Entry(self, width=30)
        self.task_entry.grid(row=0, column=0, padx=5, pady=10)
        
        # Add task button
        self.add_task_btn = ttk.Button(self, text="Add Task", command=self.add_task)
        self.add_task_btn.grid(row=0, column=1, padx=10, pady=10)
        
        # Task listbox
        self.task_listbox = Listbox(self, width=50, height=15,borderwidth=0)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        
        # Delete task button
        self.delete_task_btn = ttk.Button(self, text="Delete Task", command=self.delete_task)
        self.delete_task_btn.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    
    def add_task(self):
        task:TaskItem = TaskItem(self.task_entry.get())
        if task.get_taskitem():

            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    
    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            del self.tasks[task_index]
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")
    
    def update_task_listbox(self):
        self.task_listbox.delete(0, END)
        for task in self.tasks:
            self.task_listbox.insert(END, task.get_taskitem())
