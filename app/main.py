from fastapi import FastAPI, HTTPException
from app.models import Task
from app.crud import create_task, get_tasks, get_task, update_task, delete_task 
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "To-Do List Manager API is running."}

@app.post("/tasks", response_model=Task)
def api_create_task(task: Task):
    try:
        return create_task(task)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

@app.get("/tasks", response_model=list[Task])
def api_get_tasks():
    return get_tasks()

@app.get("/tasks/{task_id}", response_model=Task)
def api_get_task(task_id: int):
    task = get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=Task)
def api_update_task(task_id: int, updated_task: Task):
    task = update_task(task_id, updated_task)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.delete("/tasks/{task_id}", response_model=dict)
def api_delete_task(task_id: int):
    if not delete_task(task_id):
        raise HTTPException(status_code=404, detail="Task not found")
    return {"detail": "Task deleted successfully"}

app.mount("/static", StaticFiles(directory="static"), name="static")
