from datetime import datetime

class Task:
    def __init__(self, task_id=None, title="", description="", status="pending",
                 priority="medium", created_at: str = None):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.created_at = created_at or self._current_timestamp()

    @staticmethod
    def _current_timestamp():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
