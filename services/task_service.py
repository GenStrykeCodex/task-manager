from db.database import get_connection
from models.task import Task


# Adds a new task to the database
def add_task(task: Task) -> None:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO tasks (title, description, status, priority, created_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                task.title,
                task.description,
                task.status,
                task.priority,
                task.created_at
            )
        )
        conn.commit()


# Returns all tasks in the database
def get_all_tasks() -> list[Task]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        rows = cursor.fetchall()

    return [Task(*row) for row in rows]


# Returns all tasks matching the given status
def get_tasks_by_status(status: str) -> list[Task]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT task_id, title, description, status, priority, created_at
            FROM tasks
            WHERE status = ?
            ORDER BY created_at ASC
            """,
            (status,)
        )
        rows = cursor.fetchall()

    return [Task(*row) for row in rows]


# Returns all tasks matching the given priority
def get_tasks_by_priority(priority: str) -> list[Task]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT task_id, title, description, status, priority, created_at
            FROM tasks
            WHERE priority = ?
            ORDER BY created_at ASC
            """,
            (priority,)
        )
        rows = cursor.fetchall()

    return [Task(*row) for row in rows]


# Update the status of the task
def update_task_status(task_id: int, new_status: str) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tasks SET status = ? WHERE task_id = ?",
            (new_status, task_id)
        )
        conn.commit()
        return cursor.rowcount > 0


# Update the priority of the task
def update_task_priority(task_id: int, new_priority: str) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tasks SET priority = ? WHERE task_id = ?",
            (new_priority, task_id)
        )
        conn.commit()
        return cursor.rowcount > 0


# Delete a task by its ID
def delete_task(task_id: int) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM tasks WHERE task_id = ?",
            (task_id,)
        )
        conn.commit()
        return cursor.rowcount > 0
