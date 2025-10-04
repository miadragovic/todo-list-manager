import json
from app.models import Task
from typing import List

TASKS_FILE = "tasks.json"

def load_tasks() -> List[Task]:
    try:
        with open(TASKS_FILE, "r") as f:
            tasks_data = json.load(f)
            return [Task(**task) for task in tasks_data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks: List[Task]):
    with open(TASKS_FILE, "w") as f:
        json.dump([task.dict() for task in tasks], f, indent=4)
