from app.models import Task, Priority
from app.crud import create_task, get_task, get_tasks, update_task, delete_task

def setup_function():
    delete_task(999)

def teardown_function():
    delete_task(999)

def test_create_task():
    task = Task(id=999, title="Test Task", description="Description", priority=Priority.low)
    create_task(task)
    t = get_task(999)
    assert t is not None
    assert t.title == "Test Task"

def test_update_task():
    task = Task(id=999, title="Test Task", description="Description", priority=Priority.low)
    create_task(task)
    updated_task = Task(id=999, title="Updated", description="Updated desc", priority=Priority.high)
    update_task(999, updated_task)
    t = get_task(999)
    assert t is not None
    assert t.title == "Updated"

def test_delete_task():
    task = Task(id=999, title="Test Task", description="Description", priority=Priority.low)
    create_task(task)
    result = delete_task(999)
    assert result is True
    t = get_task(999)
    assert t is None
