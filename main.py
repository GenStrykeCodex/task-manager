from db.database import initialize_db, reset_database
from services.task_service import (
    add_task,
    get_all_tasks,
    get_tasks_by_status,
    get_tasks_by_priority,
    update_task_status,
    update_task_priority,
    delete_task
)

from utils.validators import (
    validate_title,
    validate_status,
    validate_priority,
    validate_task_id
)

from models.task import Task

# CONSTANTS
DEV_MODE = False
PRIORITY = ["low", "medium", "high"]
STATUS = ["pending", "completed"]
MAIN_MENU_LENGTH = 6


''' Helper Functions '''


# Create pauses between actions
def pause():
    input("Press Enter to continue...")


# Get menu choice from user
def get_choice(num: int) -> int:
    while True:
        try:
            choice = int(input(f"\nChoose an option (1-{num}): "))
            return choice

        except ValueError:
            print("Sorry! That's not an valid option.")


''' UI / Menu Functions '''


def main_menu():
    print("\n──────────────────────────")
    print("       Task Manager       ")
    print("──────────────────────────")
    print("1. Add a new task")
    print("2. View All Tasks")
    print("3. View filtered Tasks")
    print("4. Update Task Details")
    print("5. Delete Task")
    print("6. Exit")
    print("──────────────────────────")


''' Menu Handler Functions '''


# Handler function to add tasks
def add_task_handler() -> None:
    task_title = input("\nEnter the Task Title: ").lower()
    task_description = input("Enter a short Task Description: ").lower()

    print("\nPriority: ")
    for i, priority in enumerate(PRIORITY):
        print(f"{i+1}. {priority}")

    task_priority = input("\nChoose priority 'low' or 'medium' or 'high': ")

    try:
        title = validate_title(task_title)
        description = task_description
        priority = validate_priority(task_priority)
    except ValueError as e:
        print(e)
        return

    task = Task(
        title=title,
        description=description,
        priority=priority
    )

    add_task(task)
    print("\nTask Added Successfully!")


# Handler functions to view all tasks
def view_all_tasks_handler() -> None:
    tasks = get_all_tasks()

    if not tasks:
        print("No Tasks Found!")
        return

    print("\n" + "─" * 100)
    print(f"{'ID':<5} | {'Title':<15} | {'Priority':<10} | {'Status':<15} | {'Description':<20} | {'Time':<15}")
    print("─" * 100)
    for task in tasks:
        print(f"{task.task_id:<5} | {task.title:<15} | {task.priority:<10} | {task.status:<15} | {task.description:<20} | {task.created_at:<15}")
    print("─" * 100)


# Handler function for task filtering
def filter_tasks_handler(criteria: str) -> None:
    if not criteria or criteria.lower().strip() == "":
        raise ValueError("A filtering criteria must be provided.")

    if criteria.lower().strip() == "status":
        value, tasks = filter_tasks_by_status_handler()
    elif criteria.lower().strip() == "priority":
        value, tasks = filter_tasks_by_priority_handler()
    else:
        raise ValueError("Invalid Filtering Criteria!")

    print(f"\nCriteria: {criteria} | Tag: {value}")

    print("\n" + "─" * 80)
    print(f"{'ID':<5} | {'Title':<15} | {'Description':<20} | {'Time':<15}")
    print("─" * 80)
    for task in tasks:
        print(f"{task.task_id:<5} | {task.title:<15} | {task.description:<20} | {task.created_at:<15}")
    print("─" * 80)


# Handler helping functions for filter
def filter_tasks_by_status_handler() -> tuple[str, list[Task]]:
    print("\nStatus: ")
    for i, status in enumerate(STATUS):
        print(f"{i + 1}. {status}")

    while True:
        status = input("\nEnter the Task Status: ").lower()

        try:
            valid_status = validate_status(status)
            tasks = get_tasks_by_status(valid_status)
            break
        except ValueError as e:
            print(e)

    return status, tasks


def filter_tasks_by_priority_handler() -> tuple[str, list[Task]]:
    print("\nPriority: ")
    for i, priority in enumerate(PRIORITY):
        print(f"{i + 1}. {priority}")

    while True:
        priority = input("\nEnter the Task Priority: ").lower()

        try:
            valid_priority = validate_priority(priority)
            tasks = get_tasks_by_priority(valid_priority)
            break
        except ValueError as e:
            print(e)

    return priority, tasks


# Handler function to update tasks
def update_task_handler(criteria: str) -> None:
    if not criteria or criteria.lower().strip() == "":
        raise ValueError("A criteria must be provided to update task.")

    if criteria.lower().strip() == "status":
        update_task_status_handler()
    elif criteria.lower().strip() == "priority":
        update_task_priority_handler()
    else:
        raise ValueError("Invalid Criteria!")


# Handler helping functions for update
def update_task_status_handler() -> None:
    view_all_tasks_handler()
    try:
        task_id = validate_task_id(input("Enter task ID: "))
        status = validate_status(
            input("New status (pending/completed): ")
        )

        if update_task_status(task_id, status):
            print("\nTask status updated.\n")
        else:
            print("\nTask not found.\n")

    except ValueError as e:
        print(f"\n{e}")


def update_task_priority_handler() -> None:
    view_all_tasks_handler()
    try:
        task_id = validate_task_id(input("\nEnter task ID: "))
        priority = validate_priority(
            input("New priority (low/medium/high): ")
        )

        if update_task_priority(task_id, priority):
            print("\nTask priority updated.\n")
        else:
            print("\nTask not found.\n")

    except ValueError as e:
        print(f"\n{e}")


# Handler function to delete tasks
def delete_task_handler() -> None:
    view_all_tasks_handler()
    try:
        task_id = validate_task_id(input("Enter task ID: "))

        if delete_task(task_id):
            print("\nTask deleted.\n")
        else:
            print("\nTask not found.\n")

    except ValueError as e:
        print(f"\n{e}")


# Main Menu of the application
def main():
    initialize_db()

    while True:
        main_menu()

        while True:
            choice = get_choice(MAIN_MENU_LENGTH)

            if choice == 1:
                add_task_handler()
                pause()
                break

            elif choice == 2:
                view_all_tasks_handler()
                pause()
                break

            elif choice == 3:
                print("\nTwo filtering criteria are available - 'status' and 'priority'")
                criteria = input("Choose a criteria: ")

                try:
                    filter_tasks_handler(criteria)
                except ValueError as e:
                    print(e)

                pause()
                break

            elif choice == 4:
                print("\nTwo update criteria are available - 'status' and 'priority'")
                criteria = input("Choose a criteria: ")

                try:
                    update_task_handler(criteria)
                except ValueError as e:
                    print(e)

                pause()
                break

            elif choice == 5:
                delete_task_handler()
                pause()
                break

            elif choice == 6:
                print("Closing Task Manager...")
                return
            else:
                print("Sorry! This choice is not available.")


if DEV_MODE:
    confirm = input("\nDo you want to reset the database? (y/n)").lower().strip()
    if confirm == "y":
        print("\nResetting the database...")
        reset_database()
    else:
        print("\nReset Cancelled...")


if __name__ == "__main__":
    main()

print("\nThank you for using our application!")