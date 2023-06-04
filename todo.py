import json
import os
from datetime import datetime

class Task:
    def __init__(self, id, title, description, due_date):
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.filename = 'tasks.json'

        # odczytaj zadania z pliku przy uruchomieniu programu
        if os.path.isfile(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                for task_data in data:
                    task = Task(*task_data)
                    self.tasks.append(task)

        self.print_tasks()

    def add_task(self):
        id = input("Enter task ID: ")
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        due_date = input("Enter due date (YYYY-MM-DD): ")

        task = Task(id, title, description, due_date)
        self.tasks.append(task)

    def delete_task(self):
        id = input("Enter ID of task to delete: ")
        self.tasks = [task for task in self.tasks if task.id != id]

    def update_task(self):
        id = input("Enter ID of task to update: ")
        for task in self.tasks:
            if task.id == id:
                task.title = input("Enter new task title: ")
                task.description = input("Enter new task description: ")
                task.due_date = input("Enter new due date (YYYY-MM-DD): ")
                break

    def print_tasks(self):
        if self.tasks:
            print("Tasks:")
            for task in self.tasks:
                print(f"ID: {task.id}, Title: {task.title}, Due date: {task.due_date}")
        else:
            print("No tasks.")

    def print_task_detail(self):
        id = input("Enter ID of task to view details: ")
        for task in self.tasks:
            if task.id == id:
                print(f"ID: {task.id}, Title: {task.title}, Description: {task.description}, Due date: {task.due_date}")
                break

    def save_tasks(self):
        data = [task.__dict__ for task in self.tasks]
        with open(self.filename, 'w') as f:
            json.dump(data, f)

    def run(self):
        while True:
            print("\nOptions:")
            print("1. Add task")
            print("2. Delete task")
            print("3. Update task")
            print("4. View task detail")
            print("5. Save tasks")
            print("6. Exit")

            option = input("Choose an option: ")

            if option == "1":
                self.add_task()
            elif option == "2":
                self.delete_task()
            elif option == "3":
                self.update_task()
            elif option == "4":
                self.print_task_detail()
            elif option == "5":
                self.save_tasks()
            elif option == "6":
                self.save_tasks()
                break
            else:
                print("Invalid option.")

# uruchom program
to_do_list = ToDoList()
to_do_list.run()