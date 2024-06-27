import os
import json

TODO_FILE = "todo_list.json"

# Function to load tasks from a file
def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

# Function to save tasks to a file
def save_tasks(todo_list):
    with open(TODO_FILE, "w") as file:
        json.dump(todo_list, file)

# Function to display the to-do list
def display_todo_list(todo_list):
    if not todo_list:
        print("No tasks in the to-do list.")
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task['task']} - Due: {task['due_date']} - Category: {task['category']}")

# Function to add a task to the to-do list
def add_task(todo_list):
    task = input("Enter the task: ")
    due_date = input("Enter the due date (YYYY-MM-DD): ")
    category = input("Enter the category: ")
    todo_list.append({"task": task, "due_date": due_date, "category": category})
    print("Task added.")
    save_tasks(todo_list)

# Function to mark a task as done
def mark_task_done(todo_list):
    display_todo_list(todo_list)
    task_number = int(input("Enter the task number to mark as done: "))
    if 0 < task_number <= len(todo_list):
        todo_list.pop(task_number - 1)
        print("Task marked as done.")
        save_tasks(todo_list)
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task(todo_list):
    display_todo_list(todo_list)
    task_number = int(input("Enter the task number to delete: "))
    if 0 < task_number <= len(todo_list):
        todo_list.pop(task_number - 1)
        print("Task deleted.")
        save_tasks(todo_list)
    else:
        print("Invalid task number.")

# Function to filter tasks by category
def filter_tasks_by_category(todo_list):
    category = input("Enter the category to filter by: ")
    filtered_tasks = [task for task in todo_list if task['category'] == category]
    if not filtered_tasks:
        print(f"No tasks found in category: {category}")
    else:
        print(f"\nTasks in category '{category}':")
        for index, task in enumerate(filtered_tasks, start=1):
            print(f"{index}. {task['task']} - Due: {task['due_date']}")

# Main function
def main():
    todo_list = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Filter Tasks by Category")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_todo_list(todo_list)
        elif choice == "2":
            add_task(todo_list)
        elif choice == "3":
            mark_task_done(todo_list)
        elif choice == "4":
            delete_task(todo_list)
        elif choice == "5":
            filter_tasks_by_category(todo_list)
        elif choice == "6":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
