# start building task manager cli version 1.01

# taking task input
def task_input():

    priority = input("Enter the priority of task: ")
    task = input("Enter the task: ")
    save_tasks(task, priority)

# saving the tasks
def save_tasks(task,priority):

    with open("tasks.txt", "a") as file:
        file.write(f"Priority {priority}: {task}\n")

    print(f"Your task has been saved.")

    print("1. Add More Tasks (Press 1).")
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

    print("This feature is under development. It will be added soon")

# main interface
def application_home():

    print("Welcome to the Task Manager Beta 1.01!")
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