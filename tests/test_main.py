import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "To-Do List Manager API is running." in response.json()["message"]

def test_create_and_get_task():
    new_task = {
        "id": 1,
        "title": "Test task",
        "description": "A test task",
        "priority": "low"
    }
    create_resp = client.post("/tasks", json=new_task)
    assert create_resp.status_code in (200,400)

    if create_resp.status_code == 200:
        returned_task = create_resp.json()
        returned_task["title"] == "Test task"
        assert returned_task["priority"] == "low"

        all_resp = client.get("/tasks")
        assert all_resp.status_code == 200
        tasks = all_resp.json()
        assert any(task["title"] == "Test task" for task in tasks)

        get_resp = client.get(f"/tasks/{returned_task['id']}")
        assert get_resp.status_code == 200
        assert get_resp.json()["title"] == "Test task"


   

def test_update_task():
    task = {
        "id": 2,
        "title": "Update target",
        "description": "Update me",
        "priority": "medium"
    }
    client.post("/tasks", json=task)

    updated_task = {
        "id": 2,  
        "title": "Updated",
        "description": "Updated desc",
        "priority": "low"
    }
    update_resp = client.put(f"/tasks/{task['id']}", json=updated_task)
    assert update_resp.status_code == 200
    assert update_resp.json()["title"] == "Updated"
    assert update_resp.json()["priority"] == "low"

def test_delete_task():
    task = {
        "id": 3,
        "title": "Delete me",
        "description": "Will be deleted",
        "priority": "low"
    }
    client.post("/tasks", json=task)

    del_resp = client.delete(f"/tasks/{task['id']}")
    assert del_resp.status_code == 200
    assert del_resp.json()["detail"] == "Task deleted successfully"

    del_resp_404 = client.delete(f"/tasks/{task['id']}")
    assert del_resp_404.status_code == 404

def test_get_nonexistent_task():
    resp = client.get("/tasks/99999")
    assert resp.status_code == 404

def test_update_nonexistent_task():
    updated_task = {
        "id": 100,
        "title": "Nope",
        "description": "Missing",
        "priority": "low"
    }
    resp = client.put("/tasks/100", json=updated_task)
    assert resp.status_code == 404

def test_delete_nonexistent_task():
    resp = client.delete("/tasks/100500")
    assert resp.status_code == 404

def test_static_files_serving():
    resp = client.get("/static/index.html")
    assert resp.status_code in (200, 404)
