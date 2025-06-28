#Todo list application

todo_list = []

def show_menu():
    print(" To-Do List Application")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Remove a Task")
    print("4. Exit")

def add_task():
    task = input("Enter the task you want to add: ")
    todo_list.append(task)
    print(f"Task '{task}' added successfully!")

def view_tasks():
    if not todo_list:
        print("No tasks in the list.")
    else:
        print("Your To-Do List: ")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")