# start building task manager cli version 1.01
print("Welcome to the Task Manager Beta 2.10!")

# taking task input
def task_input():

    priority = input("Enter the priority of task: ")
    task = input("Enter the task: ")
    save_tasks(task, priority)

# saving the tasks
def save_tasks(task,priority):

    with open("tasks.txt", "a") as file:
        file.write(f"Priority {priority}: {task}\n")

    print(f"\nYour task has been saved.")

    print("\n1. Add More Tasks (Press 1).")
    print("2. Return to Main Menu (Press 2).")

    while True:

        option = input("Please choose an option (1-2): ")       #the user is prompted to choose an option

        if option == "1":
            task_input()

        elif option == '2':
            application_home()
        
        else:
            print('Invalid choice. Please try again.')

# managing saved tasks
def task_manage():
    
    print("\n=== TASK MANAGEMENT ===")
    print("1. Edit a Task")
    print("2. Delete a Task")
    print("3. Return to Main Menu")
    
    choice = input("Please choose an option (1-3): ")
    
    if choice == '1':
        edit_task()
    elif choice == '2':
        delete_task()
    elif choice == '3':
        application_home()
    else:
        print("Invalid choice. Please try again.")
        task_manage()


def edit_task():
    # Edit an existing task
    
    try:
        # Read all tasks from file
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        
        if not tasks:
            print("No tasks available to edit.")
            task_manage()
            return
        
        # Display all tasks with numbers
        print("\n=== Your Tasks ===")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task.strip()}")
        
        # Get task number to edit
        task_num = input("\nEnter the task number you want to edit (or 0 to cancel): ")
        
        if not task_num.isdigit():
            print("Please enter a valid number.")
            edit_task()
            return
        
        task_num = int(task_num)
        
        if task_num == 0:
            task_manage()
            return
        
        if task_num < 1 or task_num > len(tasks):
            print("Invalid task number. Please try again.")
            edit_task()
            return
        
        # Get new task details
        print(f"\nEditing: {tasks[task_num - 1].strip()}")
        new_priority = input("Enter new priority: ")
        new_task = input("Enter new task description: ")
        
        # Update the task
        tasks[task_num - 1] = f"Priority {new_priority}: {new_task}\n"
        
        # Write updated tasks back to file
        with open("tasks.txt", "w") as file:
            file.writelines(tasks)
        
        print("✓ Task updated successfully!")
        
        # Ask what to do next
        print("\n1. Edit Another Task (Press 1)")
        print("2. Return to Task Management (Press 2)")
        print("3. Return to Main Menu (Press 3)")
        
        next_action = input("Choose an option: ")
        
        if next_action == '1':
            edit_task()
        elif next_action == '2':
            task_manage()
        else:
            application_home()
    
    except FileNotFoundError:
        print("No tasks file found. Please add some tasks first.")
        application_home()


def delete_task():
    # Delete an existing task
    
    try:
        # Read all tasks from file
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        
        if not tasks:
            print("No tasks available to delete.")
            task_manage()
            return
        
        # Display all tasks with numbers
        print("\n=== YOUR TASKS ===")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task.strip()}")
        
        # Get task number to delete
        task_num = input("\nEnter the task number you want to delete (or 0 to cancel): ")
        
        if not task_num.isdigit():
            print("Please enter a valid number.")
            delete_task()
            return
        
        task_num = int(task_num)
        
        if task_num == 0:
            task_manage()
            return
        
        if task_num < 1 or task_num > len(tasks):
            print("Invalid task number. Please try again.")
            delete_task()
            return
        
        # Confirm deletion
        print(f"\nAre you sure you want to delete: {tasks[task_num - 1].strip()}")
        confirm = input("Type 'yes' to confirm: ").lower()
        
        if confirm == 'yes':
            # Remove the task
            deleted_task = tasks.pop(task_num - 1)
            
            # Write updated tasks back to file
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            
            print("✓ Task deleted successfully!")
        else:
            print("Deletion cancelled.")
        
        # Ask what to do next
        print("\n1. Delete Another Task (Press 1)")
        print("2. Return to Task Management (Press 2)")
        print("3. Return to Main Menu (Press 3)")
        
        next_action = input("Choose an option: ")
        
        if next_action == '1':
            delete_task()
        elif next_action == '2':
            task_manage()
        else:
            application_home()
    
    except FileNotFoundError:
        print("No tasks file found. Please add some tasks first.")
        application_home()

# main interface
def application_home():

    print("\n=== MAIN MENU ===")
    print("1. Add New tasks")
    print("2. View your tasks")
    print("3. Edit or Delete your tasks")
    print("4. Exit")
    
    while True:     #this loop will keep the application running until the user chooses to exit

        choice = input("Please choose an option (1-4): ")       #the user is prompted to choose an option
        
        if choice == '1':
            # Add a Task
            task_input()

        elif choice == '2':
            # View saved task
            print("Checking your tasks..")

            try:

                with open("tasks.txt", "r") as file:

                    tasks = file.readlines()

                    if tasks:
                        print("Saved Tasks:")
                        for line in tasks:
                            print(line.strip())
                    else:
                        print("No tasks saved yet.")

            except FileNotFoundError:
                print("No Tasks saved yet.")

            application_home()
        
        elif choice == '3':
            # Edit or Delete the tasks
            task_manage()

        elif choice == '4':
            # Exit the application
            print("Exiting the Task Manager. Goodbye!")
            break

        else:           # If the user enters an invalid choice

            print("Invalid choice. Please try again.")

    print("Thank you for using the Task Manager!")

application_home()