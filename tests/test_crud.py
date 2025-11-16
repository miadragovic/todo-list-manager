from app.models import Task, Priority
from app.repository import TaskRepository

repo = TaskRepository()

def setup_function():
    repo.delete_task(999)

def teardown_function():
    repo.delete_task(999)

def test_create_task():
    task = Task(id=999, title="Test Task", description="Description", priority=Priority.low)
    repo.create_task(task)
    t = repo.get_task(999)
    assert t is not None
    assert t.title == "Test Task"

def test_update_task():
    task = Task(id=999, title="Test Task", description="Description", priority=Priority.low)
    repo.create_task(task)
    updated_task = Task(id=999, title="Updated", description="Updated desc", priority=Priority.high)
    repo.update_task(999, updated_task)
    t = repo.get_task(999)
    assert t is not None
    assert t.title == "Updated"

def test_delete_task():
    task = Task(id=999, title="Test Task", description="Description", priority=Priority.low)
    repo.create_task(task)
    result = repo.delete_task(999)
    assert result is True
    t = repo.get_task(999)
    assert t is None
