# modules required
import pandas as pd
import json

# interface
menu = ('''
====== TO-DO LIST ======\n\n1. Add Task\n2. View Tasks\n3. Complete Task\n4. Edit Task\n5. Delete Task\n6. Exit
''')


# Loading data
def load_task():
    try:
        with open("my_data.json", 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        with open("my_data.json", 'w') as file:
            json.dump([], file)
        return []


def check(tasks):
    if not tasks:
        print("No tasks available")
        return False
    return True


def save_task(tasks):
    with open("my_data.json", "w") as file:
        json.dump(tasks, file, indent=4)


# All functions
def view_tasks():
    tasks = load_task()

    if not check(tasks):
        return

    df = pd.DataFrame(tasks)
    print(df)


def add_task():
    tasks = load_task()

    title = input("Enter task: ")
    status = input("Enter status (Pending/Completed): ").capitalize()

    # Check duplicate
    for task in tasks:
        if task["title"].lower() == title.lower():
            print("Task already exists.")
            return

    new_task = {
        "title": title,
        "status": status
    }

    tasks.append(new_task)
    save_task(tasks)
    print("Task added successfully.")


def edit_task():
    tasks = load_task()

    if not check(tasks):
        return

    view_tasks()

    try:
        index = int(input('Enter the task index: '))
        new_title = input("Enter new title: ")
        new_status = input("Enter new status: ").capitalize()

        # updating
        tasks[index]["title"] = new_title
        tasks[index]["status"] = new_status

        save_task(tasks)

    except ValueError:
        print("Enter a valid task number")


def complete_task():
    tasks = load_task()

    if not check(tasks):
        return

    view_tasks()

    try:
        index = int(input('Enter the task index: '))

        # Updating
        new_status = input("Enter new status: ").capitalize()
        tasks[index]["status"] = new_status

        save_task(tasks)

    except ValueError:
        print("Enter a valid task number")


def delete_task():
    tasks = load_task()

    if not check(tasks):
        return

    view_tasks()

    try:
        index = int(input('Enter the task index: '))
        tasks.pop(index)
        save_task(tasks)

    except ValueError:
        print("Enter a valid task number")


while True:
    print(menu)

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            add_task()
        case "2":
            view_tasks()
        case "3":
            complete_task()
        case "4":
            edit_task()
        case "5":
            delete_task()
        case "6":
            print("Thank you for using To-Do List.")
            break
        case _:
            print("Invalid choice. Please try again.")
