from typing import List, Optional
from app.models import Task
from app.database import load_tasks, save_tasks

# Load tasks from JSON file on module load
tasks: List[Task] = load_tasks()

def create_task(task: Task):
    tasks.append(task)
    save_tasks(tasks)
    return task

def get_tasks() -> List[Task]:
    return tasks

def get_task(task_id: int) -> Optional[Task]:
    for task in tasks:
        if task.id == task_id:
            return task 
    return None

def update_task(task_id: int, updated_task: Task):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks[i] = updated_task
            save_tasks(tasks)
            return updated_task
    return None

def delete_task(task_id: int) -> bool:
    for i, task in enumerate(tasks):
        if task.id == task_id:
            del tasks[i]
            save_tasks(tasks)
            return True
    return False
