# modules required
import pandas as pd
import json

# interface
menu = ('''
====== TO-DO LIST ======\n\n1. Add Task\n2. View Tasks\n3. Complete Task\n4. Edit Task\n5. Delete Task\n6. Exit
''')

# Loding data
def load_task():
    try:
        with open("my_data.json",'r') as file:
            return json.load(file)
    except FileNotFoundError:
        with open("my_data.json",'w') as file:
            json.dump([],file)
            return json.load(file)

def check():
    with open("my_data.json",'r') as file:
        data = json.load(file)
    if data == "[]"or data == None:
        print("No tasks available")
        return None
    return data

def save_task(tasks):
    with open("my_data.json", "w") as file:
        json.dump(tasks, file, indent=4)

# All functions
def view_tasks():
    tasks = load_task()
    if not check():
        return
    df = pd.DataFrame(tasks)
    print(df)

def add_task():
    tasks = load_task()
    if not check():
        return

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
    if not check():
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
    if not check():
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
    if not check():
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

    choice = input("Enter your choice: \n\n")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        edit_task()
    elif choice == "5":
        delete_task()
    elif choice == "6":
        print("Thank you for using To-Do List.")
        break
    else:
        print("Invalid choice. Please try again.")