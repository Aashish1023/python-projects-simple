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
    print("Task '{task}' added successfully!")

def view_tasks():
    if not todo_list:
        print("No tasks in the list.")
    else:
        print("Your To-Do List: ")
        for index, task in enumerate(todo_list, start=1):
            print("{index}. {task}")

def remove_task():
    view_tasks()
    if todo_list:
        try:
            task_num = int(input("Enter the task number you want to remove:  "))
            if 1 <= task_num <= len(todo_list):
                removed = todo_list.pop(task_num - 1)
                print(f" Removed: {removed}")
            else:
                print("❌ Invalid task number. Please try again.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

while True:
    show_menu()
    choice = input("Enter your option (1-4):")

    if choice == '1':
        add_task()
    elif choice == '2':
        add_task()
    elif choice == '3':
        add_task()
    elif choice == '4':
        print("Exiting the To-Do List Application. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please enter a number between 1 and 4.")