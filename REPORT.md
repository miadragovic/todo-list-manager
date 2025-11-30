# REPORT.md

## To-Do List Manager Version 2: Improvements and DevOps Pipeline Summary

### Student: Mia Dragovic  
### Date: November 2025

---


## Introduction
This report describes how the To‑Do List Manager API from Assignment 1 was improved using DevOps practices. The goal was not to add many new features, but to make the existing application cleaner, testable, automated, and observable.

The application is a FastAPI backend that manages to‑do items. For this assignment I worked on:
- Refactoring and code quality.
- Automated tests and coverage.
- CI with GitHub Actions.
- Docker containerization and deployment attempts to Azure.
- Health checks and metrics with Prometheus.
- Documentation.

All work is in the same GitHub repository as Assignment 1, but the structure and tooling are now more mature.

## Code quality and refactoring

At the end of Assignment 1, most logic lived directly in the FastAPI routes. Some handlers were doing input parsing, validation, business logic, and data storage in one place. This made the code harder to read and even harder to test.

For Assignment 2 I refactored the project into a clearer structure:
- app/main.py that creates the FastAPI app and defines the routes.
- app/models.py which contains Pydantic models used for request and response bodies.
- app/repository.py which handles data access for tasks (create, read, update, delete). The rest of the code uses these functions instead of directly manipulating internal data structures.

I removed repeated logic from the routes and moved it into repository‑style functions. Route handlers now mainly:
- Receive validated models.
- Call a repository function.
- Return the result or raise an HTTPException.

I also avoided scattering hardcoded values across the code. When something is used in multiple places (for example, default fields), it is defined once and reused. Overall, this made the code easier to follow and prepared it for testing.

## Testing and Coverage

Before this assignment there were no serious automated tests. I added tests using pytest:
- Unit‑style tests for the repository functions: creating, updating, deleting and listing tasks
- Integration‑style tests using FastAPI’s TestClient / httpx:
  -  Calling the main CRUD endpoints.
  - Calling /health and checking the response.
  - Checking how the API behaves with invalid input.

  Coverage is measured with coverage.py together with pytest. The command I use is:
- pytest --cov=app --cov-report=term-missing

This shows which lines are covered and produces an HTML report (screenshot provided). With the current test suite the coverage is 95%.

## Continuous Integration (CI)

To automate checks on every push, I created a GitHub Actions workflow in .github/workflows. The workflow runs on each push and pull request to the main branch.

The steps are:
1. Checkout the repository.
2. Set up Python (3.12).
3. Install dependencies from requirements.txt.
4. Run pytest with coverage.
5. Fail the job if tests fail or coverage is below the required threshold.
6. Build the Docker image for the application.

This pipeline acts as a quality gate. If tests break or coverage drops, the workflow fails and the commit is clearly marked as failing in GitHub. Only when the code passes tests and coverage does the image build step run successfully.

## Containerization and deployment work
# Docker

I wrote a Dockerfile so the app can run in a container. The Dockerfile:
- Uses a Python 3.12 base image.
- Sets /app as the working directory.
- Copies requirements.txt and installs dependencies.
- Copies the application code.
- Exposes port 80.
- Starts the app using gunicorn with the uvicorn worker:
  - gunicorn -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:80

Locally, I can run:
- docker build -t todo-local .
- docker run -p 8080:80 todo-local

With this, the API is available at http://localhost:8080/
, /docs shows the FastAPI docs, and /health returns the health status. This proves that the container image itself is correct.

# Azure deployment attempts

For the “deployment automation” requirement, I went further and integrated the container with Azure:
- The GitHub workflow builds a Docker image from the repository.
- The image is tagged and pushed to Azure Container Registry using credentials stored as GitHub secrets.
- I created an Azure Web App for Containers that pulls this image.
- I also tried a separate “code” Web App with zip deployment and a startup command.

The container works correctly on my local machine, but on the shared Azure environment the app is currently not reachable from the default domain. The logs show issues like “No module named 'uvicorn'” or “No module named 'app'” inside the Azure runtime, even though the same code and image work locally. I spent a significant amount of time trying different startup commands and layouts, but the problem seems to be specific to the platform configuration, not the code.

## Monitoring and health checks

To cover monitoring:
- I added a /health endpoint that returns a simple JSON response with the status of the service. This provides a quick way to see if the app is up.
- I integrated prometheus-fastapi-instrumentator to expose metrics at /metrics. These include:
  - Request counts per endpoint.
  - Request latency.
  - Error counts.

I created a basic Prometheus configuration file (prometheus.yml) that scrapes the /metrics endpoint from the running container. With this configuration, Prometheus sees the API as an active target and can display graphs of the collected metrics. I included screenshots of these pages for evidence.

## Documentation

I updated README.md, which now includes:
- Short project description.
- How to install dependencies.
- How to run the app with uvicorn.
- How to run tests and see coverage.
- How to build and run the Docker image.
- A quick explanation of the GitHub Actions CI workflow.
- A short note on metrics and the Prometheus setup.

This report focuses on explaining the improvements.

## Conclusion

In this assignment I took the To‑Do List Manager API from a basic working prototype to a more “DevOps‑ready” service. Overall, the project now looks and behaves much closer to a small real world service even though there is still room to improve the cloud deployment.











