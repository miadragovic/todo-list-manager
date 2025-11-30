# To-Do List Manager  
*Student: Mia Dragovic*  
*Date: November 2025*

---

## Project Overview

This repository contains version 2 of my to-do list manager. It is now built with a focus on modular, well-tested, and deployable code, featuring full DevOps workflow support. You can add, view, update, delete, and prioritize tasks using a FastAPI backend and simple HTML frontend—data persists in a local JSON file.

---

## Improvements in This Version

- Refactored using SOLID principles and modularity
- 96% test coverage using `pytest` and `coverage`
- Continuous Integration (CI) pipeline with GitHub Actions: runs all tests, measures coverage and builds the app
- Docker support for easy containerized deployment
- Integration tests for main API endpoints and backend logic
- App monitoring with Prometheus: live metrics on requests, latencies, and errors
- Documentation and step-by-step instructions for setup, test, and monitoring

---

## How to Run Locally

### Requirements

- Python 3.12 or higher
- Dependencies listed in `requirements.txt`

### Install dependencies

pip install -r requirements.txt


### Run the backend server

If `main.py` is in `app/`, run:
uvicorn app.main:app --reload


If not, run:
uvicorn main:app --reload


### Open the web interface

Go to:  
[http://127.0.0.1:8000/static/index.html](http://127.0.0.1:8000/static/index.html)

---

## Monitoring and Health Checks (Prometheus)

The app exposes:

- `/health`: basic status endpoint  
- `/metrics`: Prometheus-compatible metrics

### Running Prometheus

1. Start FastAPI server (see above).

2. In this project folder, launch Prometheus using the provided config:
prometheus.exe --config.file=prometheus.yml

3. Prometheus config (`prometheus.yml`):
global:
scrape_interval: 15s

scrape_configs:

job_name: 'prometheus'
static_configs:

targets: ['localhost:9090']

job_name: 'fastapi-app'
metrics_path: /metrics
static_configs:

targets: ['127.0.0.1:8000']

4. Access Prometheus UI:  
- Targets at: [http://localhost:9090/targets](http://localhost:9090/targets)  
- Query page at: [http://localhost:9090/graph](http://localhost:9090/graph)

Screenshots are saved in `/screenshots` folder.

---

## Running Tests and Viewing Coverage

- Tests live in `tests/`
- Run all tests and coverage report:
pytest --cov=app --cov-report=html

- Open coverage report at `htmlcov/index.html` (coverage of 96%)

---

## Docker Instructions

1. Build image:
docker build -t todo-list-manager .

2. Run container:
docker run -p 8000:80 todo-list-manager

3. Access app at:  
[http://127.0.0.1:8000/static/index.html](http://127.0.0.1:8000/static/index.html)

Monitoring endpoints: `/health` and `/metrics`

---

## Continuous Integration (CI/CD)

- GitHub Actions runs tests and coverage on every push and PR
- Pipeline fails if tests fail or coverage <70%
- View logs and artifacts on GitHub Actions tab

Current status:
- The Docker image builds and runs correctly locally.
- The image is pushed automatically to Azure Container Registry from the pipeline.
- An Azure Web App for Containers is configured to use this image, but the deployment in the shared Azure environment is currently failing with an “Application Error”. The automation and configuration are in place, but the runtime issue is still being investigated.

You can view pipeline runs and logs in the GitHub “Actions” tab.



---

## Features

- Add, view, update, delete tasks
- Assign priorities (low, medium, high)
- RESTful CRUD API
- Persistent, reliable storage
- Sort/filter by priority
- Automated tests and CI pipeline
- Live metrics monitored by Prometheus
- Health endpoint for quick status checks

---

## Non-Functional Goals

- Reliable and scalable backend
- Modular and testable code
- Deployment-ready container and pipeline
- Full observability via monitoring

---

## Development and Next Steps

- Stabilize Azure Web App deployment (image already builds and is pushed to ACR, but default domain currently shows an Application Error)
- Add Grafana dashboards for visualization (optional)
- Extend architecture towards multiple services


---

## Project Structure and SDLC

- Modularity via SOLID principles
- Incremental development with version control
- Automated CI/CD from GitHub Actions
- Docker image used as the main deployment artifact

---

**Repository contents:**
- Source code (`app/`, `main.py`)
- Prometheus config (`prometheus.yml`)
- `requirements.txt`
- Dockerfile
- Tests (`tests/`) and coverage reports (`htmlcov/`)
- Monitoring screenshots (`/screenshots`)
- Report: REPORT.md

---



