# REPORT.md

## To-Do List Manager Version 2: Improvements and DevOps Pipeline Summary

### Student: Mia Dragovic  
### Date: November 2025

---

### Overview

This report summarizes what I improved in version 2 of my To-Do List Manager project. I focused on writing cleaner code, adding automated tests, setting up continuous integration, containerizing the app with Docker, and adding monitoring with Prometheus.

---

### Key Improvements

- **Better Code Quality:**  
  I organized the code better using SOLID principles to make it easier to read and maintain.

- **Automated Testing:**  
  I added unit and integration tests that cover more than 90% of the code, with automatic coverage reports.

- **Continuous Integration (CI):**  
  I set up GitHub Actions to automatically run tests and check coverage each time I push code.  
  The pipeline stops if the tests fail or coverage is too low.

- **Containerization:**  
  I created a Dockerfile so the app can run the same everywhere whether locally or in the cloud.

- **Prometheus Monitoring:**  
  I added monitoring endpoints (`/metrics` and `/health`) to expose important app data like request counts and latency for real-time tracking with Prometheus.  
  The Prometheus config is included and working.

- **Updated Documentation:**  
  I improved the README with instructions for running, testing, monitoring, and deploying.  
  I also added screenshots showing monitoring in action.

---

### Pipeline and Deployment Status

- All code, tests, and config files are tracked in GitHub.  
- Docker makes deployment easier and more consistent.  
- Prometheus monitoring is set up and tested.  
- Azure deployment is currently on hold due to issues; will update later.

---

### Next Steps

- Finish cloud deployment after Azure issues are fixed.  
- Write more end-to-end tests.  
- Improve CI/CD pipeline for automatic full deployment.

---

### Summary

This version improves the app’s foundation with better code, testing, monitoring, and deployment capabilities.  
It prepares the project for professional-grade development and operation following DevOps best practices.

---
