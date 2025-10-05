# To-Do List Manager 
*Student: Mia Dragovic*
*Date: September 2025*


## Project Overview
I chose to build a simple to-do list manager app. This app lets users add tasks, see their tasks, update them if needed, delete tasks they don’t want, and assign a priority level to each task (like low, medium, or high). The tasks with their priorities are saved on the computer using a local file (JSON file). The app has a backend with API endpoints for these actions and a simple webpage interface. This version doesn't include user accounts or advanced features like task collaboration.

## How to Run
- Install Python 3.8+ and required packages:
pip install fastapi uvicorn pydantic
- Start the backend server:
uvicorn app.main:app --reload
- Open the frontend in your browser:
http://127.0.0.1:8000/static/index.html
- Use the web interface to manage your to-do tasks interactively.

## Technology Stack
- Backend: Python, FastAPI, Pydantic
- Frontend: HTML, CSS, JavaScript
- Storage: Local JSON file
- Tools: Git, Uvicorn

## Implemented Features
- Users can add new tasks with a title, optional details, and select a priority level.
- Users can see the full list of their tasks with priority shown.
- Users can change/update task details and priority.
- Users can delete tasks.
- Tasks and their priorities are saved persistently on disk.
- The backend API supports all core CRUD operations.
- *Implemented:* A simple user interface to interact with the tasks.
- *Implemented:* Users can sort or filter tasks by priority.

## Non-Functional Requirements
- The app responds quickly to user requests.
- All tasks and priority data persist reliably across app restarts.
- The code is clean, modular, and easy to understand.
- The app runs locally on the user's computer with no remote deployment.

## Software Development Life Cycle Model
I have used an **Agile** approach since it fits well with building the app step-by-step and allows adding and improving features gradually. I started by focusing on core functions like adding and viewing tasks, then adding priority handling and sorting later.

## Possible improvements and future works
- Add user accounts
- A real database instead of a local JSON file for better storage
- Add features such as deadlines or reminders
- More interactive frontend 
- Deploy online for wider access

## Followed Steps
1. Planning and requirements.
2. Designed the app and data structure.
3. Implemented main features (CRUD + priority).
4. Tested the app to make sure it works.
5. Wrote final documentation and reports.
6. Reflected on possible improvements and DevOps scalability.

---

