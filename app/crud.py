from typing import List, Optional
from app.models import Task
from app.database import load_tasks, save_tasks

def get_tasks() -> List[Task]:
    tasks = load_tasks()
    return tasks

def get_task(task_id: int) -> Optional[Task]:
    tasks = load_tasks()
    for task in tasks:
        if task.id == task_id:
            return task
    return None

def create_task(task: Task):
    tasks = load_tasks()
    if any(t.id == task.id for t in tasks):   
        raise ValueError("Task with this ID already exists")
    tasks.append(task)
    save_tasks(tasks)
    return task

def update_task(task_id: int, updated_task: Task):
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks[i] = updated_task
            save_tasks(tasks)
            return updated_task
    return None

def delete_task(task_id: int) -> bool:
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        if task.id == task_id:
            del tasks[i]
            save_tasks(tasks)
            return True
    return False
