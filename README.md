# To-Do List Manager — SDLC Checkpoint 1
*Author: [Your Name]*
*Date: September 2025*

## Introduction
This document outlines the planning phase of the To-Do List Manager project. It covers project scope, functional and non-functional requirements, and the selected software development life cycle (SDLC) approach.

## Project Scope
I chose to build a simple to-do list manager app. This app lets users add tasks, see their tasks, update them if needed, delete tasks they don’t want, and assign a priority level to each task (like low, medium, or high). The tasks with their priorities will be saved on the computer using a local file (like a JSON file) or a small database (SQLite). The app will have a backend with API endpoints for these actions and maybe a simple webpage interface. This version will not include user accounts or advanced features like task collaboration.

## Functional Requirements
- Users can add new tasks with a title, optional details, and select a priority level.
- Users can see the full list of their tasks with priority shown.
- Users can change/update task details and priority.
- Users can delete tasks.
- Tasks and their priorities are saved permanently on the local machine.
- The app provides basic API endpoints for all these actions.
- *Optional:* A simple user interface to interact with the tasks.
- *Optional:* Users can sort or filter tasks by priority.

## Non-Functional Requirements
- The app should respond quickly, ideally within one second for requests.
- The tasks and priorities should not be lost when the app closes and restarts.
- The code should be clean, modular, and easy to understand.
- The app will run locally on my computer; no remote deployment yet.
- Git will be used for version control with meaningful commits.

## Software Development Life Cycle Model
I will use an **Agile** approach since it fits well with building the app step-by-step and allows adding and improving features gradually. I will start by focusing on core functions like adding and viewing tasks, then add priority handling and sorting later.

## Planned Steps
1. Planning and requirements (now).
2. Designing the app and data structure.
3. Implementation of main features (CRUD + priority).
4. Testing the app to make sure it works.
5. Writing final documentation and reports.
6. Reflecting on possible improvements and DevOps scalability.

---

*This plan serves as the foundation for the project and will be updated as development progresses in future checkpoints.*
