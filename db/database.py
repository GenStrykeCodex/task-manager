import sqlite3
from pathlib import Path
from sqlite3 import Connection, Error

# Database file path
DB_PATH = Path("data/tasks.db")


# Returns a SQLite database connection.
def get_connection() -> Connection:
    try:
        DB_PATH.parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row  # Enables dict-like row access
        return conn
    except Error as e:
        raise RuntimeError(f"Database connection failed: {e}")


# Creates required tables if they don't exist.
def initialize_db() -> None:
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS tasks (
                    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    status TEXT CHECK(status IN ('pending', 'completed')) NOT NULL,
                    priority TEXT CHECK(priority IN ('low', 'medium', 'high')) NOT NULL,
                    created_at TEXT NOT NULL
                )
                """
            )
            conn.commit()
    except Error as e:
        raise RuntimeError(f"Database initialization failed: {e}")


# Verifies that the database and required tables exist.
def check_database() -> bool:
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name='tasks';"
            )
            return cursor.fetchone() is not None
    except Error:
        return False


def reset_database() -> None:
    """
    Deletes the database file safely.
    Useful for development resets.
    """
    if DB_PATH.exists():
        DB_PATH.unlink()
