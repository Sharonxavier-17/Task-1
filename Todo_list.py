# To-Do List Application

# Define the list to store tasks
todo_list = []

# Function to display the current to-do list
def display_tasks():
    if not todo_list:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")
    print("\n")

# Function to add a new task
def add_task():
    task = input("Enter a new task: ")
    todo_list.append(task)
    print(f"Task '{task}' has been added to the list.\n")

# Function to remove a task
def remove_task():
    display_tasks()
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 0 < task_num <= len(todo_list):
            removed_task = todo_list.pop(task_num - 1)
            print(f"Task '{removed_task}' has been removed from the list.\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")

# Function to update a task
def update_task():
    display_tasks()
    try:
        task_num = int(input("Enter the task number to update: "))
        if 0 < task_num <= len(todo_list):
            new_task = input("Enter the updated task: ")
            todo_list[task_num - 1] = new_task
            print(f"Task {task_num} has been updated to '{new_task}'.\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")

# Main menu for the application
def main_menu():
    while True:
        print("To-Do List Menu:")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Update a task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            update_task()
        elif choice == '5':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a valid option.\n")

# Run the To-Do List application
if __name__ == "__main__":
    main_menu()
