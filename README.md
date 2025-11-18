# To-Do List Manager  
*Student: Mia Dragovic*  
*Date: November 2025*

---

## Project Overview

This app is version 2 of my original to-do list manager. Now, it’s built with a focus on clean code, testing, automation, and DevOps best practices. You can still add, view, update, delete, and prioritize tasks, but this version is better tested, containerized with Docker, and ready for deployment. The app uses a FastAPI backend with a simple frontend webpage. Data is stored locally in a JSON file.

---

## Improvements in This Version

- Code refactored for clarity and modularity, following SOLID principles
- Tests cover API endpoints and backend functions, with over 90% code coverage
- Automated test and coverage reporting using GitHub Actions (CI pipeline)
- Dockerfile to run the app in a container, plus workflows for CI Docker build/test
- HTML test coverage report included in the repo (`htmlcov` folder)
- Ready for cloud deployment (pending platform details)
- Documentation updated for all steps

---

## How to Run Locally

1. **Requirements**
   - Python 3.12 or higher
   - All dependencies listed in `requirements.txt`

2. **Install dependencies**  
pip install -r requirements.txt


3. **Start the backend server**  
uvicorn app.main:app --reload


4. **Open the web interface**  
Go to [http://127.0.0.1:8000/static/index.html](http://127.0.0.1:8000/static/index.html)

---

## Running Tests and Viewing Coverage

- Automated tests use `pytest`, coverage measurement uses `coverage`.
- Run all tests with:
pytest --cov=app --cov-report=html

- After running, open `htmlcov/index.html` for detailed coverage report (should be >90%).

---

## Project Technology

- **Backend:** Python, FastAPI, Pydantic
- **Frontend:** HTML, CSS, JS
- **Storage:** Local JSON file
- **DevOps Tools:** Docker, GitHub Actions, pytest, coverage

---

## Docker Instructions

1. **Build the Docker image:**
docker build -t todo-list-manager .


2. **Run as a Docker container:**
docker run -p 8000:8000 todo-list-manager


3. **Access the app:**  
[http://127.0.0.1:8000/static/index.html](http://127.0.0.1:8000/static/index.html)  
Endpoints (for integration or monitoring):  
- `/health` (status check, adds soon)
- `/metrics` (Prometheus monitoring, adds soon)

---

## Continuous Integration (CI)

- All pushes/PRs to main trigger automated tests and build in GitHub Actions
- Pipeline fails if tests do not pass or code coverage drops below 70%
- See test logs and coverage in the Actions tab on GitHub

---

## Features

- Add, view, update, delete tasks
- Assign priorities (low, medium, high)
- Tasks saved persistently
- RESTful API for all CRUD operations
- Sort and filter tasks by priority
- Automated tests and code coverage reporting

---

## Non-Functional Goals

- Responsive and reliable backend
- Data persists across restarts
- Modular, well-tested code
- Containerized for easy deployment

---

## SDLC Used

Agile approach: planned, implemented, reviewed, and improved in steps. Each assignment stage led to new improvements and features, all version-controlled on GitHub.

---

## Test Coverage

- Achieves >95% code coverage (see `htmlcov/index.html`)
- Automated test report included in repo
- Coverage and tests run on every push/PR

---

## Improvements and Next Steps

- Add `/health` and `/metrics` endpoints for monitoring and cloud readiness
- Integrate Prometheus/Grafana for app metrics
- Automate deployment to cloud (details pending)
- Write a short report (REPORT.md) summarizing project improvements and pipeline

---

## How This Was Built

1. Refactored code for modularity and SOLID principles
2. Added end-to-end and unit tests for key functionality
3. Measured and improved code coverage
4. Containerized with Docker for easy deployment
5. Set up automated CI pipeline for tests and coverage
6. Updated documentation with clear run/test/deploy steps



