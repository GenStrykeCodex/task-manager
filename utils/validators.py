def validate_title(title: str) -> str:
    if not title or not title.strip():
        raise ValueError("Task title cannot be empty.")
    return title.strip()


def validate_status(status: str) -> str:
    status = status.lower().strip()
    if status not in {"pending", "completed"}:
        raise ValueError("Status must be 'pending' or 'completed'.")
    return status


def validate_priority(priority: str) -> str:
    priority = priority.lower().strip()
    if priority not in {"low", "medium", "high"}:
        raise ValueError("Priority must be low, medium, or high.")
    return priority


def validate_task_id(task_id: str) -> int:
    if not task_id.isdigit():
        raise ValueError("Task ID must be a positive number.")
    task_id = int(task_id)
    if task_id <= 0:
        raise ValueError("Task ID must be greater than zero.")
    return task_id
